import React, { useState, useEffect } from 'react';
import Chart from 'react-apexcharts';
import './Dashboard.css';

const BirthDefect = ({ selectedSource, selctedType, selectedClassType }) => {

    const Port = process.env.REACT_APP_API_KEY;
    const accessToken = localStorage.getItem('token');

    const options = {
        dataLabels: {
            enabled: false,
        },
        legend: {
            show: false,
        },
        colors: ['#E8007D'],
        labels: ['Yes', 'No'],
    };

    const [chartData, setChartData] = useState({
        options: {
            dataLabels: {
                enabled: false,
            },
            legend: {
                show: false,
            },
            labels: ['Birth Defect'],

            colors: ['#E8007D'],
        },
        series: [0, 0],
    });

    useEffect(() => {
        const fetchData = async () => {
            if (selectedSource && selctedType && selectedClassType) {
                try {
                    const apiUrl = `${Port}/Screening/birth-defects/count/${selectedSource}/${selctedType}/${selectedClassType}/`;
                    console.log('API URL:', apiUrl);

                    const response = await fetch(apiUrl,
                        {
                          headers: {
                            Authorization: `Bearer ${accessToken}`
                          }
                        });

                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }

                    const data = await response.json();
                    console.log('API Data:', data);

                    const series = [data.birth_defects_count];

                    setChartData((prevChartData) => ({
                        ...prevChartData,
                        series,
                    }));
                } catch (error) {
                    console.error('Error fetching data:', error);
                }
            }
            else if (selectedSource && selctedType) {
                try {
                    const apiUrl = `${Port}/Screening/birth-defects/count/${selectedSource}/${selctedType}/`;
                    console.log('API URL:', apiUrl);

                    const response = await fetch(apiUrl,
                        {
                          headers: {
                            Authorization: `Bearer ${accessToken}`
                          }
                        });

                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }

                    const data = await response.json();
                    console.log('API Data:', data);

                    const series = [data.birth_defects_count];

                    setChartData((prevChartData) => ({
                        ...prevChartData,
                        series,
                    }));
                } catch (error) {
                    console.error('Error fetching data:', error);
                }
            }
        };

        fetchData();
    }, [selectedSource, selctedType, selectedClassType, Port]);

    return (
        <div className="donut-container bbiorthhhhhhhhhhhhh">
            <h5 className="birthdashboard">Birth Defect</h5>
            <Chart options={chartData.options} series={chartData.series} type="donut" width="200" height='150' />
        </div>
    );
}

export default BirthDefect;
