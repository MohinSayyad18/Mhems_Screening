// import React, { useState, useEffect } from 'react';
// import './Sidebar.css';
// import { Link } from 'react-router-dom';
// import SpaceDashboardIcon from '@mui/icons-material/SpaceDashboard';
// import PersonAddAltOutlinedIcon from '@mui/icons-material/PersonAddAltOutlined';
// import SummarizeIcon from '@mui/icons-material/Summarize';
// // import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
// // import ExpandLessIcon from '@mui/icons-material/ExpandLess';
// import CoPresentIcon from '@mui/icons-material/CoPresent';
// import MapsHomeWorkIcon from '@mui/icons-material/MapsHomeWork';
// import HealthAndSafetyIcon from '@mui/icons-material/HealthAndSafety';
// import sperologo from '../../Images/SPERO-Final-logo png (1) 2.png'
// import GroupAddOutlinedIcon from '@mui/icons-material/GroupAddOutlined';
// import FollowTheSignsIcon from '@mui/icons-material/FollowTheSigns';

// const Sidebarnew = () => {

//   const [selectedItem, setSelectedItem] = useState('Dashboard');
//   const [hoveredItem, setHoveredItem] = useState('');
//   const [permission, setPermission] = useState([])
//   const [clickedItem, setClickedItem] = useState('');

//   const handleItemClick = (itemName) => {
//     setSelectedItem(itemName);
//     setClickedItem(itemName);
//   };

//   const handleItemHover = (itemName) => {
//     setHoveredItem(itemName);
//   };

//   useEffect(() => {
//     const storedPermissions = localStorage.getItem('permissions');
//     // console.log('Stored Permissions:', storedPermissions);
//     const parsedPermissions = storedPermissions ? JSON.parse(storedPermissions) : [];
//     // console.log('parsedPermissions Permissions:', storedPermissions);
//     setPermission(parsedPermissions);
//   }, []);

//   const iconMapping = {
//     Dashboard: <SpaceDashboardIcon />,
//     Citizen: <PersonAddAltOutlinedIcon />,
//     Source: <PersonAddAltOutlinedIcon />,
//     'Schedule Screening': <SummarizeIcon />,
//     Report: <SummarizeIcon />,
//     Screening: <CoPresentIcon />,
//     Source: <MapsHomeWorkIcon />,
//     HealthCard: <HealthAndSafetyIcon />,
//     // Healthcard: <GroupAddOutlinedIcon />,
//     'System User': <SummarizeIcon />,
//     Permission: <SummarizeIcon />,
//     'Follow-Up' : <FollowTheSignsIcon/>
//   };


//   return (
//     <div>
//       <aside className='main-sidebar elevation-3'>
//         <div className='sidebar'>
//           <nav className='mt-2'>
//             <ul className='nav nav-sidebar flex-column' data-widget='treeview' role='menu'>
//               {
//                 permission.map((module, index) => {
//                   return (
//                     <li key={index} className={`nav-item listview ${selectedItem === module.moduleName ? 'active' : ''}`}>
//                       {module.modules_submodule.map((submodule, subIndex) => (
//                         <Link
//                           key={subIndex}
//                           className={`nav-link ${hoveredItem === submodule.moduleName ? 'hovered' : ''} ${clickedItem === submodule.moduleName ? 'clicked' : ''}`}
//                           id='list'
//                           to={`/mainscreen/${submodule.moduleName}`}
//                           onClick={() => handleItemClick(submodule.moduleName)}
//                           onMouseEnter={() => handleItemHover(submodule.moduleName)}
//                           onMouseLeave={() => handleItemHover('')}
//                         >
//                           {iconMapping[submodule.moduleName] && React.cloneElement(iconMapping[submodule.moduleName], {
//                             style: {
//                               color: clickedItem === submodule.moduleName ? 'white' : 'black',
//                               marginRight: '.5rem',
//                               transition: 'color 0.3s', // Add transition for a smooth color change
//                             },
//                           })}
//                           <p className='ptag' style={{ color: clickedItem === submodule.moduleName ? 'white' : 'black' }}>
//                             {submodule.moduleName}
//                           </p>
//                         </Link>

//                       ))}
//                     </li>
//                   );
//                 })

//               }
//             </ul>
//           </nav>
//         </div>
//       </aside>
//     </div>
//   );
// };

// export default Sidebarnew;

import React, { useState, useEffect } from 'react';
import './Sidebar.css';
import { Link } from 'react-router-dom';
import SpaceDashboardIcon from '@mui/icons-material/SpaceDashboard';
import PersonAddAltOutlinedIcon from '@mui/icons-material/PersonAddAltOutlined';
import SummarizeIcon from '@mui/icons-material/Summarize';
import CoPresentIcon from '@mui/icons-material/CoPresent';
import MapsHomeWorkIcon from '@mui/icons-material/MapsHomeWork';
import HealthAndSafetyIcon from '@mui/icons-material/HealthAndSafety';
import FollowTheSignsIcon from '@mui/icons-material/FollowTheSigns';
import sperologo from '../../Images/SPERO-Final-logo png (1) 2.png';
import GroupAddOutlinedIcon from '@mui/icons-material/GroupAddOutlined';

const Sidebarnew = () => {
  const [selectedItem, setSelectedItem] = useState('Dashboard');
  const [hoveredItem, setHoveredItem] = useState('');
  const [permission, setPermission] = useState([]);
  const [clickedItem, setClickedItem] = useState('');

  const handleItemClick = (itemName) => {
    setSelectedItem(itemName);
    setClickedItem(itemName);
  };

  const handleItemHover = (itemName) => {
    setHoveredItem(itemName);
  };

  useEffect(() => {
    const storedPermissions = localStorage.getItem('permissions');
    const parsedPermissions = storedPermissions ? JSON.parse(storedPermissions) : [];
    setPermission(parsedPermissions);
  }, []);

  const iconMapping = {
    Dashboard: <SpaceDashboardIcon />,
    Citizen: <PersonAddAltOutlinedIcon />,
    Source: <PersonAddAltOutlinedIcon />,
    'Schedule Screening': <SummarizeIcon />,
    Report: <SummarizeIcon />,
    Screening: <CoPresentIcon />,
    Source: <MapsHomeWorkIcon />,
    HealthCard: <HealthAndSafetyIcon />,
    'System User': <SummarizeIcon />,
    Permission: <SummarizeIcon />,
    'Follow-Up': <FollowTheSignsIcon />,
    // Remove the 'Investigation' module from the iconMapping
  };

  return (
    <div>
      <aside className='main-sidebar elevation-3'>
        <div className='sidebar'>
          <nav className='mt-2'>
            <ul className='nav nav-sidebar flex-column' data-widget='treeview' role='menu'>
              {permission.map((module, index) => {
                return (
                  <li key={index} className={`nav-item listview ${selectedItem === module.moduleName ? 'active' : ''}`}>
                    {module.modules_submodule.map((submodule, subIndex) => (
                      // Exclude 'Investigation' module from rendering
                      submodule.moduleName !== 'Investigation' && (
                        <Link
                          key={subIndex}
                          className={`nav-link ${hoveredItem === submodule.moduleName ? 'hovered' : ''} ${clickedItem === submodule.moduleName ? 'clicked' : ''}`}
                          id='list'
                          to={`/mainscreen/${submodule.moduleName}`}
                          onClick={() => handleItemClick(submodule.moduleName)}
                          onMouseEnter={() => handleItemHover(submodule.moduleName)}
                          onMouseLeave={() => handleItemHover('')}
                        >
                          {iconMapping[submodule.moduleName] && React.cloneElement(iconMapping[submodule.moduleName], {
                            style: {
                              color: clickedItem === submodule.moduleName ? 'white' : 'black',
                              marginRight: '.5rem',
                              transition: 'color 0.3s', // Add transition for a smooth color change
                            },
                          })}
                          <p className='ptag' style={{ color: clickedItem === submodule.moduleName ? 'white' : 'black' }}>
                            {submodule.moduleName}
                          </p>
                        </Link>
                      )
                    ))}
                  </li>
                );
              })}
            </ul>
          </nav>
        </div>
      </aside>
    </div>
  );
};

export default Sidebarnew;

