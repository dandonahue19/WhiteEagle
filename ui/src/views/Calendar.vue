<template>
  <div class="calendar">
    <h1 class="header">Calendar</h1>
    <div class="calendarWrapper">
      <div class="options">
        <v-btn  outlined class="mr-4" @click="setToday">
          Today
        </v-btn>
        <v-btn fab text small @click="prev">
          <v-icon small>
            mdi-chevron-left
          </v-icon>
        </v-btn>
        <p class="month" v-if="this.$refs.calendar">{{ this.$refs.calendar.title }}</p>
        <v-btn fab text small  @click="next">
          <v-icon small>
            mdi-chevron-right
          </v-icon>
        </v-btn>
      </div>
     
      <v-calendar
          ref="calendar"
          v-model="focus"
          :events="events"
          :event-color="getEventColor"
          @change="calendarChange"
          color="primary"
        ></v-calendar>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import moment from 'moment';

export default {
  name: "Calendar",
  components: {
  },
  data() {
    return {
      focus: '',
      loadedInterval:null,
      events: [],
    }
  },
  created(){
    
  },
  computed: {
    title: function(){
      console.log('title')
      if(this.$refs.calendar){
        return this.$refs.calendar.title
      }
      return ''
    }
  },
  mounted () {
    this.$refs.calendar.checkChange()
  },
  methods:{
    setToday () {
      console.log('today')
      this.focus = ''
    },
    prev () {
      console.log('prev')
      this.$refs.calendar.prev()
    },
    next () {
      console.log('next')
      this.$refs.calendar.next()
    },
    getEventColor (event) {
      console.log(event.color)
      return event.color
    },
    calendarChange(interval){
      console.log(interval)
      this.getMonthlyEvents(interval)
    },
    getMonthlyEvents(interval){
      if(!this.loadedInterval || interval.start.date != this.loadedInterval.start.date){
        this.events = []
        this.loadedInterval = interval
        let  query = `{
          events{
            id,
            name
            dt
            dtEnd
            reoccuring
            dow
            time
            description
            location
            type{
              name
              color
              id
            }
          }
        }`
        this.$axios.get('graphql', {params:{query}}).then((res) => {
          res.data.data.events.forEach((event) => {
            if (event.reoccuring){
              let start = moment(interval.start.date).startOf('week')
              let end = moment(interval.end.date).endOf('week')
              console.log(start, end)
              while(start<end){
                console.log(`${start.toDate()}T${event.time}`)
                let eventStart = start.clone().add(event.dow, 'd')
                this.events.push({
                  name: event.name,
                  start: eventStart.toDate(),
                  end: eventStart.clone().add(1, 'h').toDate(),
                  color: event.type.color
                })
                start.add(1, 'w')
              }
            }
          })
        })
      }
    }
  }
};
</script>
<style lang="scss">
.calendar{
  display: flex;
  flex-direction: column;
  height: 100%;
  max-height: calc(100vh - 15rem);
  overflow-y: auto;
  z-index: 999;
  .calendarWrapper{
    margin: 2rem ;
    height: 75%;
    .options{
      display: flex;
      align-items: center;
      color: white;
      margin-bottom: 1rem;
      i, .v-btn{
        color:white;
      }
      p{
        margin: 0;
        letter-spacing: 2px;
        font-size: 1.5rem;
      }
    }
  }
}
</style>
