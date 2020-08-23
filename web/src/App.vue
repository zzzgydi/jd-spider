<template>
  <div class="container">
    <h1>商品信息收集</h1>
    <div class="box" v-for="(res, idx) in results" :key="idx">
      <result-box :mallName="res.name" :itemList="res.item_list" :errList="res.err_list" />
    </div>
  </div>
</template>

<script>
import ResultBox from "./components/ResultBox.vue";
import axios from "axios";

export default {
  name: "App",
  components: {
    ResultBox,
  },
  data() {
    return {
      results: [],
    };
  },
  beforeMount() {
    axios.get("http://localhost:7788/get_data").then((res) => {
      const { data } = res;
      this.results = data;
    });
  },
};
</script>

<style lang="scss">
.container {
  margin: 0 auto 0;

  h1 {
    text-align: center;
    margin-bottom: 20px;
  }
}
</style>
