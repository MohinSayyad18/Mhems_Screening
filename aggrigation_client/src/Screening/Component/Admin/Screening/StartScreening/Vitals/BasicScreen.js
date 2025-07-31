import React, { useEffect, useState } from 'react'
import './BasicScreen.css'
import Generalexam from './BasiScreen/Generalexam'
import Systematic from './BasiScreen/Systematic'
import Disiability from './BasiScreen/Disiability'
import Birthdefect from './BasiScreen/Birthdefect'
import Childhood from './BasiScreen/Childhood'
import Difieciency from './BasiScreen/Difieciency'
import Skin from './BasiScreen/Skin'
import Checkbox from './BasiScreen/Checkbox'
import Diagnosis from './BasiScreen/Diagnosis'
import Treatment from './BasiScreen/Treatment'
import Femalescreening from './BasiScreen/Femalescreening'
import BadHabits from './BasiScreen/BadHabits'

const BasicScreen = ({ pkid, citizensPkId, gender, scheduleID, citizenidddddddd, fetchVital }) => {

  const userID = localStorage.getItem('userID');
  console.log(userID);
  console.log(scheduleID, 'scheduleIDddd');
  console.log(citizenidddddddd, 'aaaaaaaaj');
  const userGroup = localStorage.getItem('usergrp');

  //// access the source from local storage
  const SourceUrlId = localStorage.getItem('loginSource');

  //// access the source name from local storage
  const SourceNameUrlId = localStorage.getItem('SourceNameFetched');

  useEffect(() => {
    console.log('User Group:', userGroup);
  }, [userGroup]);

  const commonOptions = [
    { id: 1, name: 'General Examination' },
    { id: 10, name: 'Treatment' },
    ...(gender === 1 ? [{ id: 12, name: 'Female Child Screening' }] : []), // Add Female Child Screening if gender is 1
  ];

  const expertOptions = [
    { id: 1, name: 'General Examination' },
    { id: 2, name: 'Systemic Exam' },
    { id: 3, name: 'Disability Screening' },
    { id: 4, name: 'Birth Defects' },
    { id: 5, name: 'Childhood disease' },
    { id: 6, name: 'Deficiencies' },
    { id: 7, name: 'Skin Condition' },
    { id: 8, name: 'Check Box if Normal' },
    { id: 9, name: 'Diagnosis' },
    { id: 10, name: 'Treatment' },
    { id: 11, name: 'Bad Habit' },
    ...(gender === 2 ? [{ id: 12, name: 'Female Child Screening' }] : []), // Add Female Child Screening if gender is 1
  ];

  const options = userGroup === 'UG-DOCTOR' ? commonOptions : expertOptions;

  const [selectedTab, setSelectedTab] = useState('General Examination');

  const [basicScreeningPkId, setBasicScreeningPkId] = useState(null); // State to store basic_screening_pk_id

  const handleTabClick = (tabName, basicScreeningPkId) => {
    if (gender === 1 && selectedTab === 'Treatment' && tabName === 'Female Child Screening') {
      return;
    }

    setSelectedTab(tabName);
    setBasicScreeningPkId(basicScreeningPkId);
  };

  const [openedPart, setOpenedPart] = useState('childInfo'); // Initial section

  const handleMoveToImmunisation = () => {
    setOpenedPart('immunizationsection'); // Replace with your actual state update logic
  };

  return (
    <div>
      <div className="row scroll">
        <div className="col-md-2" style={{ height: "100vh" }}>
          <div className="card generalcard" style={{ height: "100%" }}>
            <div style={{ height: "100%" }}>
              <h5 className="basictitle">Basic Screening</h5>
              <div>
                {options.map((option) => (
                  <div key={option.id} onClick={() => handleTabClick(option.name)}>
                    <h5 className={`generaltitle ${selectedTab === option.name ? 'selected-general' : ''}`}>
                      {option.name}
                    </h5>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>

        <div className="col-md-10">
          <div className="card basicscreentabbbbb" style={{ height: "100%" }}>
            {selectedTab ? (
              <div className="content contenttype" id="generalContent">
                {selectedTab === 'General Examination' && (
                  <Generalexam
                    pkid={pkid}
                    citizensPkId={citizensPkId} scheduleID={scheduleID} citizenidddddddd={citizenidddddddd}
                    onAcceptClick={(tabName, basicScreeningPkId) => handleTabClick(tabName, basicScreeningPkId)}
                  />
                )}

                {selectedTab === 'Treatment' && (
                  <Treatment pkid={pkid} citizensPkId={citizensPkId}
                    basicScreeningPkId={basicScreeningPkId} scheduleID={scheduleID} citizenidddddddd={citizenidddddddd}
                    onAcceptClick={(tabName, basicScreeningPkId) => handleTabClick(tabName, basicScreeningPkId)} />
                )}

                {selectedTab === 'Systemic Exam' && (
                  <Systematic pkid={pkid} citizensPkId={citizensPkId}
                    basicScreeningPkId={basicScreeningPkId} scheduleID={scheduleID} citizenidddddddd={citizenidddddddd}
                    onAcceptClick={(tabName, basicScreeningPkId) => handleTabClick(tabName, basicScreeningPkId)} />
                )}

                {selectedTab === 'Disability Screening' && (
                  <Disiability pkid={pkid} citizensPkId={citizensPkId}
                    basicScreeningPkId={basicScreeningPkId} scheduleID={scheduleID} citizenidddddddd={citizenidddddddd}
                    onAcceptClick={(tabName, basicScreeningPkId) => handleTabClick(tabName, basicScreeningPkId)} />
                )}

                {selectedTab === 'Birth Defects' && (
                  <Birthdefect pkid={pkid} citizensPkId={citizensPkId} citizenidddddddd={citizenidddddddd}
                    basicScreeningPkId={basicScreeningPkId} scheduleID={scheduleID}
                    onAcceptClick={(tabName, basicScreeningPkId) => handleTabClick(tabName, basicScreeningPkId)} />
                )}

                {selectedTab === 'Childhood disease' && (
                  <Childhood pkid={pkid} citizensPkId={citizensPkId} citizenidddddddd={citizenidddddddd}
                    basicScreeningPkId={basicScreeningPkId} scheduleID={scheduleID}
                    onAcceptClick={(tabName, basicScreeningPkId) => handleTabClick(tabName, basicScreeningPkId)} />
                )}

                {selectedTab === 'Deficiencies' && (
                  <Difieciency pkid={pkid} citizensPkId={citizensPkId} citizenidddddddd={citizenidddddddd}
                    basicScreeningPkId={basicScreeningPkId} scheduleID={scheduleID}
                    onAcceptClick={(tabName, basicScreeningPkId) => handleTabClick(tabName, basicScreeningPkId)} />
                )}

                {selectedTab === 'Skin Condition' && (
                  <Skin pkid={pkid} citizensPkId={citizensPkId} citizenidddddddd={citizenidddddddd}
                    basicScreeningPkId={basicScreeningPkId} scheduleID={scheduleID}
                    onAcceptClick={(tabName, basicScreeningPkId) => handleTabClick(tabName, basicScreeningPkId)} />
                )}

                {selectedTab === 'Check Box if Normal' && (
                  <Checkbox pkid={pkid} citizensPkId={citizensPkId} citizenidddddddd={citizenidddddddd}
                    basicScreeningPkId={basicScreeningPkId} scheduleID={scheduleID}
                    onAcceptClick={(tabName, basicScreeningPkId) => handleTabClick(tabName, basicScreeningPkId)} />
                )}

                {selectedTab === 'Diagnosis' && (
                  <Diagnosis pkid={pkid} citizensPkId={citizensPkId} citizenidddddddd={citizenidddddddd}
                    basicScreeningPkId={basicScreeningPkId} scheduleID={scheduleID}
                    onAcceptClick={(tabName, basicScreeningPkId) => handleTabClick(tabName, basicScreeningPkId)}
                  />
                )}

                {
                  selectedTab === 'Female Child Screening' && (
                    <Femalescreening pkid={pkid} citizensPkId={citizensPkId} citizenidddddddd={citizenidddddddd}
                      basicScreeningPkId={basicScreeningPkId} scheduleID={scheduleID}
                      onAcceptClick={(tabName, basicScreeningPkId) => handleTabClick(tabName, basicScreeningPkId)}
                    />
                  )
                }
                {
                  selectedTab === 'Bad Habit' && (
                    <BadHabits pkid={pkid} citizensPkId={citizensPkId} citizenidddddddd={citizenidddddddd}
                      basicScreeningPkId={basicScreeningPkId} scheduleID={scheduleID}
                      onAcceptClick={(tabName, basicScreeningPkId) => handleTabClick(tabName, basicScreeningPkId)}
                    />
                  )
                }

              </div>
            ) : null}
          </div>
        </div>

        {/* <div className="row">
          <button type="button" className="btn btn-sm acceptbasicscreen">Accept</button>
        </div> */}
      </div>
    </div>
  )
}

export default BasicScreen
