import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Pft = ({ citizensPkId, pkid, nextVitalName, fetchVital, onMoveToVital}) => {

    //__________________________Vital START
    console.log(nextVitalName, 'dental fetching current componenet.....');
    // console.log(nextEmergencyVital, 'fetching the vital Name from the previous Componenet');
    const [nextVitalName9, setNextVitalName9] = useState('');

    useEffect(() => {
        if (fetchVital && Array.isArray(fetchVital)) {
            // Find the index of the current nextEmergencyVital
            const currentPartIndex = fetchVital.findIndex(vital => vital.screening_list === nextVitalName);

            // If the current part name is found, get the next vital
            if (currentPartIndex !== -1 && currentPartIndex + 1 < fetchVital.length) {
                const nextVitalName = fetchVital[currentPartIndex + 1];
                setNextVitalName9(nextVitalName.screening_list); // Update the state with the next vital name
            } else {
                setNextVitalName9(''); // Clear the state if no next vital is available or current part name is not found
            }
        } else {
            setNextVitalName9(''); // Clear the state if fetchVital is not valid
        }
    }, [fetchVital, nextVitalName]);
    //__________________________Vital END

    console.log(pkid, 'pft pk id fetching......');
    const [pftReading, setPftReading] = useState('');
    const [pftRemark, setPftRemark] = useState('');
    const accessToken = localStorage.getItem('token');
    const userID = localStorage.getItem('userID');
    console.log(userID);

    const Port = process.env.REACT_APP_API_KEY;

    useEffect(() => {
        if (pftReading) {
            const fetchData = async () => {
                try {
                    const response = await axios.get(`${Port}/Screening/pft/${pftReading}/`, {
                        headers: {
                            Authorization: `Bearer ${accessToken}`
                        }
                    });
                    console.log(response.data);
                    setPftRemark(response.data);
                } catch (error) {
                    console.error('Error:', error);
                }
            };
            fetchData();
        }
    }, [pftReading]);

    const handleReadingChange = (event) => {
        const newReading = event.target.value;
        // Check if the new reading is a valid number, not negative, and within the desired range (0 to 800)
        if (!isNaN(newReading) && newReading >= 0 && newReading <= 800) {
            // If valid, update the state
            setPftReading(newReading);
            // Clear observation if PFT reading is cleared
            if (newReading === '') {
                setPftRemark('');
            }
        } else {
            // Show alert for invalid input
            alert('PFT Reading should not be greater than 800');
            setPftReading('');
            setPftRemark('');
        }
    };

    const handleSubmit = async () => {
        const isConfirmed = window.confirm('Submit PFT Form');
        const confirmationStatus = isConfirmed ? 'True' : 'False';

        try {
            const response = await axios.post(`${Port}/Screening/citizen_pft_info/${pkid}`, {
                citizen_pk_id: citizensPkId,
                pft_reading: pftReading,
                observations: pftRemark.message,
                added_by: userID,
                modify_by: userID,
                form_submit: confirmationStatus,
            }, {
                headers: {
                    Authorization: `Bearer ${accessToken}`
                }
            });
            console.log('Response from POST API:', response.data);
            onMoveToVital (nextVitalName9);
        } catch (error) {
            console.error('Error submitting PFT data:', error);
        }
    };

    useEffect(() => {
        const fetchFormData = async () => {
            try {
                const response = await axios.get(`${Port}/Screening/pft_info_get/${pkid}`, {
                    headers: {
                        Authorization: `Bearer ${accessToken}`
                    }
                });
                console.log(response.data);
                // Check if response data is not empty
                if (response.data.length > 0) {
                    // Set PFT reading state based on fetched data
                    setPftReading(response.data[0].pft_reading);
                    // Set PFT remark state based on fetched data
                    setPftRemark(response.data[0].observations);
                } else {
                    // If response data is empty, clear states
                    setPftReading('');
                    setPftRemark('');
                }
            } catch (error) {
                console.error('Error:', error);
            }
        };
        fetchFormData();
    }, [pkid, accessToken, Port]);

    return (
        <div>
            <div>
                <div className="row backdesign">
                    <div className="col-md-12">
                        <div className="card bmicard">
                            <div className="row">
                                <div className="col-md-4">
                                    <h6 className='mt-1 familyTital'>PFT INFORMATION</h6>
                                </div>
                                <div className="col-md-5 ml-auto">
                                    <div class="progress-barbmi"></div>
                                </div>
                            </div>
                        </div>

                        <div className="card grothcardmonitor">
                            <div className="row">
                                <div className="col-md-12">
                                    <h6 className="BMITitle">PFT</h6>
                                    <div className="childdetailelement"></div>
                                </div>

                                <div className="col-md-3 ml-2">
                                    <label className="visually-hidden remarkvision">PFT Reading</label>
                                    <input
                                        className='form-control inputvision'
                                        placeholder='Reading'
                                        name='pft_reading'
                                        value={pftReading}
                                        type='number'
                                        onChange={handleReadingChange}
                                    />
                                </div>

                                <div className="col-md-3 ml-2">
                                    <label className="visually-hidden remarkvision">PFT Remarks</label>
                                    <input
                                        className='form-control inputvision'
                                        name='observations'
                                        value={pftRemark ? pftRemark.message || '' : ''}
                                        style={{
                                            backgroundColor: pftRemark && pftRemark.message && pftRemark.message.trim() === 'Danger' ? 'Red' :
                                                pftRemark && pftRemark.message && pftRemark.message.trim() === 'Caution' ? 'yellow' :
                                                    pftRemark && pftRemark.message && pftRemark.message.trim() === 'Stable' ? 'green' :
                                                        pftRemark && pftRemark.message && pftRemark.message.trim() === 'Out Of Range' ? 'darkbrown' :
                                                            'inherit',
                                            color: 'black'
                                        }}
                                        readOnly
                                    />
                                </div>

                            </div>

                            <div className="row mb-4 mt-4">
                                <button
                                    type="button"
                                    className="btn btn-sm submitvital"
                                    onClick={handleSubmit}
                                >
                                    Submit
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Pft
