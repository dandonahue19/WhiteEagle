<template>
  <div class="about" :class="{'focused': enlargedSection}">
    <div class="section school"
      :class="{'shrunk': enlargedSection, 'enlarged': enlargedSection=='school'}"
      @click="enlargeSection('school')">
      <div class="section-card">
        <h1 class="header">School</h1>
        <p class="schoolDescription">Sed ut perspiciatis unde omnis iste natus error 
          sit voluptatem accusantium doloremque laudantium, 
          totam rem aperiam, eaque ipsa quae ab illo inventore
          veritatis et quasi architecto beatae vitae dicta sunt 
          explicabo. Nemo enim ipsam voluptatem quia voluptas sit 
          aspernatur aut odit aut fugit, sed quia consequuntur magni 
          dolores eos qui ratione voluptatem sequi nesciunt. Neque porro
            quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur,
            adipisci velit, sed quia non numquam eius modi tempora
              incidunt ut labore et dolore magnam aliquam quaerat voluptatem.
              Ut enim ad minima veniam, quis nostrum exercitationem ullam 
              corporis suscipit laboriosam, nisi ut aliquid ex ea commodi 
              consequatur? Quis autem vel eum iure reprehenderit qui in ea 
              voluptate velit esse quam nihil molestiae consequatur, 
          vel illum qui dolorem eum fugiat quo voluptas nulla p
          ariatur</p>
          <div class="photo">
            <img src="../assets/master.jpg" alt=""/>
          </div> 
      </div>
    </div>
    <div class="section masters"
      :class="{'shrunk': enlargedSection, 'enlarged': enlargedSection=='masters'}"
       @click="enlargeSection('masters')">
      <div class="section-card">
        <h1 class="header">Masters</h1>
        <div :class="['master', master.class]" v-for="master in masters" :key="master.name">
          <div class="text">
            <h3>{{master.name}}</h3>
            <p>{{master.description}}</p>
          </div> 
          <div class="photo">
            <img src="../assets/master.jpg" alt=""/>
          </div> 
          <div class="belt">
          </div>
        </div>
      </div>
    </div>
    <div class="section instructors"
      :class="{'shrunk': enlargedSection, 'enlarged': enlargedSection=='instructors'}"
      @click="enlargeSection('instructors')">
      <div class="section-card">
        <h1 class="header">Instructors</h1>
        <div :class="['instructor', instructor.class]" v-for="instructor in instructors" :key="instructor.name">
          <div class="text">
            <h3>{{instructor.name}}</h3>
            <p>{{instructor.description}}</p>
          </div> 
          <div class="photo">
            <img src="../assets/master.jpg" alt=""/>
          </div> 
          <div class="belt">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "About",
  components: {
  },
  data() {
    return {
      masters: [
        {name: 'Master Donahue',
        description: 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur',
        class: 'master',
        },
      ],
      instructors: [
        {name: 'Master Donahue',
        description: 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur',
        class: 'master',
        },
      ],
      enlargedSection: null,
    }
  },
  methods: {
    enlargeSection(section){
      if (section!=this.enlargedSection){
        this.enlargedSection=section;
      }
      else{
        this.enlargedSection = false;
      }
    }
  }
};
</script>
<style lang="scss">
.about{
  display: flex;
  flex-direction: column;
  max-height: 100%;
  height: 100%;
  overflow-y: auto;
  padding-bottom: 0;
  transition: all .25s ease-in-out;
  background: #131d28;
  &.focused{
    padding-bottom: 75px;
  }
  .section{
    position: relative;
    transition: all .25s ease-in-out;
    height: 30%;
    width: calc(100% - 2rem);
    background: #2a3950;
    border-radius: 25px 0 0 25px; 
    margin: 0.5rem 2rem;
    margin-right: 0;   
    cursor: pointer;
    .text, p{
      display: none;;
    }
    &.shrunk{
      height: 4rem;
      .text, p{
        display: inline-block;
      }
      .photo{
        opacity: .4;
      }
    }
    &.enlarged{
      height: calc(100% - 8rem);
      .photo{
        opacity: .8;
        height: 200px;
        overflow: hidden;
      }
    }
    &:before {
      position: absolute;
      border-radius: 25px 0 0 25px;
      z-index: 1;
      top: -1px;
      left: -1px;
      width: 100%;
      height: 100%;
      background: linear-gradient(171deg, #ffffff8a, transparent 52%, transparent 100%);
      content: "";
    }
    .section-card{
      height: 100%;
      overflow-y: auto;
      position: relative;
      background: #2a3950;
      padding: 0.5rem 2rem;
      z-index: 2;
      border-radius: 25px 0 0 25px;
      &:before {
        position: absolute;
        border-radius: 25px 0 0 25px;
        z-index: 1;
        top: -1px;
        left: -1px;
        width: 100%;
        height: 100%;
        background: linear-gradient(171deg, #ffffff21, transparent 50%, transparent 100%);
        content: "";
      }
      .header{
        margin: 0rem;
        color: white;
      }
      .photo{
        transition: all .25s ease-in-out;
        position: absolute;
        text-align: center;
        top: 0;
        left: 0;
        width: 100%;
        z-index: -1;
        img{
          max-width: 100%;
        }
      }
    }
  }
  .schoolDescription{
    color: white;
    padding: 2rem;
    letter-spacing: 1px;
    font-weight: 100;
  }
  .instructorHeader{
    margin-left: 100px;
    font-size: 3rem;
    opacity: .8;
    color: #A5DEF1;
    letter-spacing: 9px;
    text-shadow: 
      -2px 2px 4px rgb(29 38 50 / 35%), 
      2px -2px 4px rgb(205 228 255 /25%), 
      1px -1px 3px rgb(205 228 255 / 25%),
      -1px 1px 3px rgb(29 38 50 / 35%);
    
    font-weight: 100;
    z-index: 10;
  }
  .instructors, .masters{
    .instructor, .master{
      display: flex;
      border-radius: 5px;
      height: 400px;
      color: white;
      .text{
        width: 100%;
        width: calc(100% - 4rem);
        position: absolute;
        top: 153px;
        h3{
          margin: 0rem;
          font-size: 2rem;
        }
      }
      .master{
        .belt{
          background-color: black;
        }
      }
    }
  }
}
@media(max-width: 1000px){
  .about{

  }
}
</style>
