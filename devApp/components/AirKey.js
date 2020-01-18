import React from 'react';
import Box from "@material-ui/core/Box";
import AppBar from "@material-ui/core/AppBar";
import Trainer from "./trainer/trainer" 


import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';

export default class AirKey extends React.Component {
	constructor(props) {
		super(props);

		this.state = {

		}
	}

	render() {
		return (
			<Box>
				<AppBar position="static">
					<Toolbar>
						<IconButton edge="start" color="inherit" aria-label="menu">
							<MenuIcon />
						</IconButton>
					
						<Typography variant="h6">
							News
						</Typography>
					</Toolbar>
				</AppBar>

				<Trainer />
			</Box>
		);
	}
}