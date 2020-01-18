import React from "react";

import Grid from "@material-ui/core/Grid";
import Box from "@material-ui/core/Box";
import TextField from "@material-ui/core/TextField";

const possibleKeys = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'], ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'], ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '?']];

function KeyIcon(props) {
	console.log(props.selected);
	return (
		<Box style={ props.selected ? {"backgroundColor": "lightblue"} : {"backgroundColor": "white"} }>
			{props.letter}
		</Box>
	)
}

function KeyboardRow(props) {
	return (
		<Grid container spacing={3}>
			{
				props.keys.map((key) => {
					return (
						<Grid key={key} item xs={1}>
							<KeyIcon letter={key} selected={key.toLowerCase() == props.selectedKey.toLowerCase() }/>
						</Grid>
					);
				})
			}
		</Grid>
	)
}

export default class Keyboard extends React.Component {
	constructor(props) {
		super(props);

		this.state = {
			keys: possibleKeys,
			selectedKey: "",
		}
	}

	render() {
		return (
			<Box>
				<Box>
					{
						this.state.keys.map((keyRow, index) => {
							return <KeyboardRow keys={keyRow} selectedKey={this.state.selectedKey} />;
						})
					}
				</Box>

				<TextField onKeyPress={(event) => {
					this.props.keyPressed(event.key);
					
					this.setState({
						selectedKey: event.key
					});
				}} />
			</Box>
		);
	}


}