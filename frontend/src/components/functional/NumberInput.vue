<!-- Component to add/substract certain parameters.

How to use:

<NumberInput :min = 5 :max = 10></NumberInput>
min nad max are optional, to define limits of the changer

<NumberInput
      v-for="item in fetchedItems"
      :key="item.id"
      :value="item.someValue"
    ></NumberInput>
-->

<template>
  <div style="text-align: center;">
    <div style="text-align:center; font-style: oblique; font-weight: 600;">{{ isMobile ? name.substring(0, 3).toUpperCase() : name }}</div>
    <button
      class="value-control"
      v-if="!isMobile"
      @click="stepDown"
      title="Decrease value"
      aria-label="Decrease value"
    >
      -
    </button>

    <input
      class="value-input"
      type="number"
      v-model="inputValue"
      name="numberInput"
      :min="min"
      :max="max"
      @input="onInput"
      ref="inputRef"
      id="numberInput"
    />

    <button
      class="value-control"
      v-if="!isMobile"
      @click="stepUp"
      title="Increase value"
      aria-label="Increase value"
    >
      +
    </button>
  </div>
</template>

<style scoped>
.value-control {
  justify-content: center;
  margin: 0 0.1rem;
  padding: 0.5rem;
  background: transparent;
  border: 0.1rem solid #817474;
  border-radius: 0.3rem;
  color: #6c5c5c;
  cursor: pointer;
}

.value-control:hover {
  background: #eee;
}

.value-control:active {
  background: #ddd;
}

.value-control:focus,
.value-input:focus {
  outline: 2px solid #b90606;
  outline-offset: 1px;
}

.value-input {
  justify-content: center;
  margin: 0;
  width: 35%;
  border: 0.3rem double red;
  border-radius: 0.8rem;
  padding: 0.5rem;
  text-align: center;
}

.value-input:hover {
  border-color: #777;
}

/* Chrome, Safari, Edge, Opera */
input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Firefox */
input[type="number"] {
  -moz-appearance: textfield;
}

@media (max-width: 768px) {
  input[type="number"]::-webkit-outer-spin-button,
  input[type="number"]::-webkit-inner-spin-button {
    -webkit-appearance: auto;
    padding: 0;
  }

  input[type="number"] {
    padding: 0;
    width: 90%;
  }

  .value-control {
    display: none;
  }
}
</style>

<script>
export default {
  props: {
    min: {
      type: Number,
      default: 0, // Default min value
    },
    max: {
      type: Number,
      default: 99, // Default max value
    },
    value: {
      type: Number,
    },
    name: {
      type: String,
      default: "Empty label",
    },
  },
  data() {
    return {
      inputValue: this.value,
      isMobile: window.innerWidth <= 768, // Detect mobile screen size
    };
  },
  watch: {
    value(newVal) {
      this.inputValue = newVal;
    },
    inputValue(newVal) {
      this.$emit("update:value", newVal);
    },
  },
  methods: {
    onInput(event) {
      let value = Number(event.target.value);
      if (isNaN(value)) value = this.min;

      if (value < this.min) value = this.min;
      if (value > this.max) value = this.max;

      this.inputValue = value;
    },
    stepUp() {
      const input = this.$refs.inputRef;
      if (input && typeof input.stepUp === 'function') {
        input.stepUp();
        this.inputValue = Number(input.value);
      }
    },
    stepDown() {
      const input = this.$refs.inputRef;
      if (input && typeof input.stepDown === 'function') {
        input.stepDown();
        this.inputValue = Number(input.value);
      }
    },
    checkIfMobile() {
      this.isMobile = window.innerWidth <= 768;
    },
  },
  mounted() {
    window.addEventListener("resize", this.checkIfMobile);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.checkIfMobile);
  },
};
</script>
