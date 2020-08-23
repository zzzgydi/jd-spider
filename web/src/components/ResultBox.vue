<template>
  <div class="result-box">
    <div class="result-header">
      <h2>{{ mallName }}</h2>
      <div class="button-groups">
        <button class="clip-button" :data-clipboard-text="tableHtml" @click="copyTableHtml">复制表格</button>
        <button @click="isShowData = !isShowData">{{ cShowDataBtn }}</button>
        <button @click="isShowErr = !isShowErr">
          {{ cShowErrBtn }}
        </button>
      </div>
    </div>
    <div v-show="isShowData" class="result-table">
      <table border="1">
        <thead>
          <td v-for="th in tableHead" :key="th">{{ th }}</td>
        </thead>
        <tbody>
          <tr v-for="(row, idx) in itemList" :key="idx">
            <td class="td-index">{{ idx + 1 }}</td>
            <td class="td-name">{{ row.sku_name }}</td>
            <td class="td-price">{{ row.cur_price }}</td>
            <td class="td-price">{{ row.old_price }}</td>
            <td class="td-price">{{ row.plus_price }}</td>
            <td class="td-act">{{ row.activity_type }}</td>
            <td class="td-quan">
              <ul>
                <li v-for="(quan, qid) in row.quan_items" :key="qid">{{ quan }}</li>
              </ul>
            </td>
            <td class="td-prom">
              <ul>
                <li v-for="(prom, pid) in row.prom_items" :key="pid">{{ prom }}</li>
              </ul>
            </td>
            <td class="td-link"><a :href="row.sku_url" target="_blank">点击跳转</a></td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-show="isShowErr" class="result-error">
      <h3>{{ cShowErrTitle }}</h3>
      <ul>
        <li v-for="(err, idx) in errList" :key="idx">{{ err }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import clipboard from "clipboard";

export default {
  name: "ResultBox",
  props: {
    mallName: String,
    itemList: Array,
    errList: Array,
  },
  data() {
    return {
      tableHead: "序号 商品名称 当前价格 原价格 Plus价格 活动类型 优惠券 促销 商品链接".split(" "),
      tableHtml: "",
      isShowData: true,
      isShowErr: false,
    };
  },
  computed: {
    cShowDataBtn() {
      return this.isShowData ? "隐藏数据" : "显示数据";
    },
    cShowErrBtn() {
      return this.isShowErr ? "收起" : "显示错误";
    },
    cShowErrTitle() {
      return this.errList.length > 0 ? "错误信息" : "无错误";
    },
  },
  beforeMount() {
    // 处理html
    const tableHead = "商品名称 当前价格 原价格 PLUS价格 活动类型 优惠券 促销 商品链接"
      .split(" ")
      .map((e) => `<td>${e}</td>`)
      .join("");
    const rowData = [];
    for (const item of this.itemList) {
      const { sku_name, cur_price, old_price, plus_price, activity_type, quan_items, prom_items, sku_url } = item;
      const quan = "<ul>" + quan_items.map((e) => `<li>${e}</li>`).join("") + "</ul>";
      const prom = "<ul>" + prom_items.map((e) => `<li>${e}</li>`).join("") + "</ul>";
      const url = `<a href="${sku_url}" target="_blank">点击跳转</a>`;
      const data = [sku_name, cur_price, old_price, plus_price, activity_type, quan, prom, url];
      const dataStr = data.map((e) => `<td>${e}</td>`).join("");
      rowData.push(`<tr>${dataStr}</tr>`);
    }
    this.tableHtml = `<table border="1"><thead>${tableHead}</thead><tbody>${rowData.join("")}</tbody></table>`;
  },
  methods: {
    copyTableHtml() {
      const clip = new clipboard(".clip-button");
      clip.on("success", function() {
        console.log("复制成功");
      });
      clip.on("error", function() {
        console.log("复制失败");
      });
    },
  },
};
</script>

<style lang="scss">
.result-box {
  padding: 0 10px 15px;
  width: 1100px;
  // background-color: red;
  font-size: 16px;
  margin: 0 auto 20px;
  border-bottom: 1px solid #e5e5e5;

  .result-header {
    display: flex;
    justify-content: space-between;
    align-items: center;

    h2 {
      padding: 10px;
      font-size: 24px;
      font-weight: normal;
      text-align: left;
    }

    .button-groups {
      button {
        width: 80px;
        text-align: center;
        user-select: none;
        color: #606266;
        border: 1px solid #e5e5e5;
        padding: 6px 10px;
        border-radius: 6px;
        outline: none;
        cursor: pointer;

        &:hover {
          box-shadow: 1px 1px 6px 1px rgba(#000, 0.05);
        }
      }
      button + button {
        margin-left: 15px;
      }
    }
  }

  .result-table {
    margin: 5px auto 0;

    // 边框
    table,
    thead,
    tbody,
    tr,
    td {
      border-color: #d5d5d5;
    }

    table {
      width: 100%;
      text-align: left;
      border-collapse: collapse;

      thead {
        td {
          padding: 15px 6px;
          color: #909399;
        }
      }

      tbody {
        td {
          padding: 6px 4px;
          line-height: 24px;
          word-break: break-all;
          word-wrap: break-word;
        }

        .td-index {
          width: 30px;
          text-align: center;
        }

        .td-name {
          width: 270px;
        }

        .td-price {
          width: 70px;
          font-size: 18px;
          text-align: center;
        }

        .td-act {
          width: 80px;
        }

        .td-quan {
          width: 100px;
        }

        .td-link {
          width: 70px;
          text-align: center;
        }
      }
    }
  }

  .result-error {
    margin: 20px auto 0;
    width: 100%;
    border: 1px solid #999999;
    color: #606266;

    h3 {
      color: red;
      font-weight: normal;
      text-align: left;
      padding: 10px 20px;
      border-bottom: 1px solid #d5d5d5;
    }

    ul {
      padding: 10px 20px;
      li {
        margin-bottom: 8px;

        &:last-child {
          margin-bottom: 0;
        }
      }
    }
  }

  ul {
    list-style: none;

    li {
      &::before {
        content: "";
        display: inline-block;
        width: 6px;
        height: 6px;
        background-color: #909399;
        border-radius: 50%;
        margin-right: 4px;
        margin-bottom: 2px;
      }
    }
  }
}
</style>
