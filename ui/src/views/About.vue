<template>
  <div class="about">
    <h1 class="header">Our School</h1>
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
    <div class="instructors">
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
</template>

<script>
// @ is an alias to /src

export default {
  name: "About",
  components: {
  },
  data() {
    return {
      instructors: [
        {name: 'Master Donahue',
        description: 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur',
        class: 'master',
        },
      ]
    }
  }
};
</script>
<style lang="scss">
.about{
  display: flex;
  flex-direction: column;
  max-height: calc(100vh - 15rem);
  overflow-y: auto;
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
  .instructors{
    .instructor{
      display: flex;
      padding: 1rem;
      margin: 2rem;
      border-radius: 5px;
      height: 400px;
      background-color: rgba(255, 255, 255, 0.842);
      .text{
        width: 50%;
        h3{
          font-size: 2rem;
        }
      }
      .photo{
        width: 50%;
        height: 100%;
        text-align: center;
        img{
          max-width: 100%;
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
</style>
