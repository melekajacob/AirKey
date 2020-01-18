import React from "react";
// import fileSystem from "fs";
import Box from "@material-ui/core/Box";
import Keyboard from "./keyboard";

const getResistanceValues = () => {
	return [0, 0, 0, 0, 0, 0, 0, 0];
}

export default class Trainer extends React.Component {
	constructor(props) {
		super(props);
	}

	render() {
		return (
			<Box>
				<Keyboard keyPressed={(key) => {

				}} />
			</Box>
		);
	}
}