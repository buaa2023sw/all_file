<template>
  <div class="home">
    <div class="header">头部</div>
    <template v-if="show">
      <div class="header">
        <router-link to="/customerHome"
                     class="header-title">
          电商网站首页
        </router-link>
        <br><br>
        <!--搜索框-->
        <div class="searchBox">
          <input type="text" v-model="inputText" placeholder="请输入关键词进行搜索" class="searchInput" style="padding-left: 10px;">
          <input type="button"  @click="Click" value="搜索" class="searchButton">
        </div>
        <div class="header-menu" style="float: right">
          <v-avatar color="teal" size="48">
            <span class="white--text headline">{{this.user}}</span>
          </v-avatar>
        </div>
        <br><br>
        <customerList></customerList>
      </div>
      <router-view></router-view>
    </template>
    <!-- 挂载所有路由 -->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  components: {

  },
  data(){

  },
  methods: {

  },
}
</script>

<style scoped>
.header {
  position: absolute;
  line-height: 40px;
  top: 0px;
  left: 0px;
  right: 0px;
}
body{
  margin:0;
}

.searchBox{
  margin: 0 auto;
  width: 40%;
  position: relative;
}
.searchInput{
  display: inline-block;
  width: 85%;
  height: 38px;
  border: 1px solid #cccccc;
  float: left;
  box-sizing: border-box;
  -moz-box-sizing:border-box; /* Firefox */
  -webkit-box-sizing:border-box; /* Safari */
  border-bottom-left-radius: 5px;
  border-top-left-radius: 5px;
}
.searchButton{
  display: inline-block;
  width: 10%;
  height: 38px;
  line-height: 40px;
  float: left;
  background-color: #00a0e9;
  font-size: 16px;
  cursor: pointer;
  border-bottom-right-radius: 5px;
  border-top-right-radius: 5px;
  border: none;
  color: #fff;
}


.container {
  width: 5000px;
  margin: 50px auto;
  overflow: hidden;
  border: 1px solid #fdfdfe;
  position: center;

}
.search_bar1 {
  background-color: rgb(63, 150, 245);
  height: 50px;
  width:800px;
  overflow: hidden;
  border-radius: 3px;
  margin-left: 200px;
  box-sizing: border-box;
  padding: 5px;}
input {
  width: 100%;
  height: 40px;
  box-sizing: border-box;
  border: 0;
  border-radius: 3px;
  margin: 0;
  padding: 0px 40px 0px 10px;
  outline: 0;
  font-size: 14px;
  color: #949494;
  background-color: #fff;
}
input::-webkit-input-placeholder {
  color: #8c8c8c;
}
</style>