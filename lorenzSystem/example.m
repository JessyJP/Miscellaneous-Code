close all;
clear all;
clc;
% Lorenz system parameters
sigma = 10;
rho = 28;
beta = 8/3;

% Initial conditions
r0 = [1; 1; 1]; % [x0; y0; z0]

% Time span for the simulation
tspan = [0 100];

% Solve the Lorenz system
[t, r] = ode45(@(t, z) lorenzSystem(t, z, sigma, rho, beta), tspan, r0);

% Plot the solution
figure;
plot3(r(:,1), r(:,2), r(:,3));
title('Lorenz Attractor');
xlabel('X');
ylabel('Y');
zlabel('Z');
grid on;
view(3); % Adjust the viewing angle for better visualization

%% Animate and Write to Video
clf; % Clear the current figure

saveVideoON = true;

if (saveVideoON)
    % Set up video writer
    videoFileName = 'LorenzAttractorAnimation.mp4';
    vw = VideoWriter(videoFileName, 'MPEG-4'); % Specify MPEG-4 format for MP4
    vw.FrameRate = 2*50; % Set frame rate
    vw.Quality = 100; % Set the quality (0 to 100, where 100 is the highest quality)
    open(vw);
end

% Lorenz system parameters
sigma = 10;
rho = 28;
beta = 8/3;

% Initial conditions
r0 = [1; 1; 1]; % [x0; y0; z0]
time = linspace(0, 100, 5000 + 1);

% Set up the plot and make the figure full screen
fig = gcf;
set(fig, 'Units', 'normalized', 'Position', [0 0 1 1]); % Make figure full screen
axis tight manual % this ensures that getframe() returns a consistent size
beginPT = plot3(r0(1), r0(2), r0(3), '*g');
hold on;
currPT = plot3(r0(1), r0(2), r0(3), '*r');
title('Lorenz Attractor');
xlabel('x');
ylabel('y');
zlabel('z');
grid on;
view(3); % Adjust the viewing angle for better visualization
ax = gca;
% Create an animated line object
h = animatedline('Color', 'b', 'LineWidth', 1);

% Loop through time steps
for i = 2:numel(time)
    % Time span for the current step
    tspan = [time(i-1) time(i)];
    
    % Solve the Lorenz system for the current time span
    [t, r] = ode45(@(t, z) lorenzSystem(t, z, sigma, rho, beta), tspan, r0);
    
    % Update the initial condition for the next step
    r0 = r(end, :)';
    
    % Add points to the animated line
    addpoints(h, r(:,1), r(:,2), r(:,3));

    % Plot end point
    currPT.XData = r(end,1);
    currPT.YData = r(end,2);
    currPT.ZData = r(end,3);
    
    % Update the title with the current time step
    title(sprintf('Lorenz Attractor [t = %.2fs]', t(end)));
    view(10*i/180,30);
    % Force MATLAB to redraw the figure
    drawnow;
    
    % Capture the plot as an image frame
    if (saveVideoON)
        frame = getframe(gcf);
        writeVideo(vw, frame);
    end
end

if (saveVideoON)
    % Close the video file
    close(vw);
    
    % Inform the user
    disp(['Video saved as ', videoFileName]);
end

