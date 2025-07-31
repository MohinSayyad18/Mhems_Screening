import React, { useState, useEffect } from 'react';
import Chart from 'react-apexcharts';

const Psychological = ({ selectedSource, selctedType, selectedClassType }) => {
  const [data, setData] = useState([]);
  const Port = process.env.REACT_APP_API_KEY;
  const accessToken = localStorage.getItem('token');

  const source = localStorage.getItem('loginSource');

  console.log(source, 'fetched source in the PFT');

  useEffect(() => {
    const fetchData = async () => {
      if (selectedSource && selctedType && selectedClassType) {
        try {
          const res = await fetch(`${Port}/Screening/psyco-count/${selectedSource}/${selctedType}/${selectedClassType}/`, {
            headers: {
              Authorization: `Bearer ${accessToken}`
            }
          });
          const apiData = await res.json();
          setData(apiData);
          console.log(apiData);
        } catch (error) {
          console.error("Error Data:", error);
        }
      } else if (selectedSource && selctedType) {
        try {
          const res = await fetch(`${Port}/Screening/psyco-count/${selectedSource}/${selctedType}/`, {
            headers: {
              Authorization: `Bearer ${accessToken}`
            }
          });
          const apiData = await res.json();
          setData(apiData);
          console.log(apiData);
        } catch (error) {
          console.error("Error Data:", error);
        }
      }
    };
    fetchData();
  }, [selectedSource, selctedType, selectedClassType, accessToken]);

  const xAxisCategories = source === '1' ?
    ['Reading', 'Writing', 'Hyper', 'Aggressive'] :
    ['PFT Reading', 'PFT Remark'];

  const options = {
    chart: {
      type: 'bar',
      horizontal: true,
      toolbar: {
        show: false,
      },
    },
    plotOptions: {
      bar: {
        horizontal: true,
        dataLabels: {
          position: 'top',
        },
      },
    },
    dataLabels: {
      enabled: false,
    },
    // xaxis: {
    //     categories: ['Reading', 'Writing', 'Hyper', 'Aggressive'],
    // },
    xaxis: {
      categories: xAxisCategories, // Set x-axis categories dynamically
    },
    yaxis: {
      min: 0,
      max: 200,
    },
    grid: {
      show: false,
    },
  };

  const getColorByIndex = (index) => {
    const colors = ['#F72585', '#B5179E', '#7209B7', '#3F37C9'];
    return colors[index % colors.length];
  };

  const series = [
    {
      data: Object.keys(data).map((key, index) => ({
        x: key,
        y: data[key],
        fillColor: getColorByIndex(index),
      })),
    },
  ];

  return (
    <div className="donut-container">
      <h5 className="birthdashboard">
        {
          source === '1' ? 'Psychological Screening' : 'PFT'
        }
      </h5>
      <Chart options={options} series={series} type="bar" height="200" />
    </div>
  );
};

export default Psychological;
