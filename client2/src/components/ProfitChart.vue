<script>
import { Line, mixins } from 'vue-chartjs'
const {reactiveProp} = mixins


export default {
  extends: Line,
  mixins: [reactiveProp],
  props: {
    labels: {
      type: Array,
      required: true
    },
    title: {
      type: String,
      required: true
    },
    dataType: {
      type: String,
      required: true
    }
  },
  mounted() {
    let vue = this
    this.renderChart(
        {
          labels: this.labels,
          datasets: [
            {
              label: 'Data 1',
              data: this.chartData,
              backgroundColor: 'transparent',
              borderColor: 'rgba(1, 116, 188, 0.50)',
              pointBackgroundColor: 'rgba(171, 71, 188, 1)'
            }
          ]
        },
        {
          responsive: true,
          maintainAspectRatio: false,
          title: {
            display: true,
            text: this.title
          },
          legend: {display: false},
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true,
                callback(value) {
                  /*if(parseInt(value) >= 1000){
                    return '$' + value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                  } else {
                    return '$' + value;
                  }*/
                  console.log(this)
                  return `${value} ${vue.dataType}`
                }
              }
            }]
          }
        }
    )
  }
}
</script>