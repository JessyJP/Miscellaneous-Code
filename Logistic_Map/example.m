% Parameters for the sweep
r_min = 2.4; % Minimum value of r to consider
r_max = 4.0; % Maximum value of r to consider
r_steps = 1000; % Number of steps in r
x0 = 0.5; % Initial population ratio
n = 1000; % Total number of generations to simulate
discard = 800; % Number of generations to discard

% Preallocate array for speed
rs = linspace(r_min, r_max, r_steps);
final_xs = zeros(length(rs), n-discard);

% Perform the sweep
for i = 1:length(rs)
    r = rs(i);
    x = logisticMap(r, x0, n);
    final_xs(i, :) = x(end-(n-discard-1):end); % Take the last k values
end

% Plotting
figure;
hold on;
for i = 1:length(rs)
    plot(rs(i) * ones(1, n-discard), final_xs(i, :), 'b.', 'MarkerSize', 1);
end
title('Bifurcation Diagram of the Logistic Map');
xlabel('Growth Rate r');
ylabel('Population Ratio');
hold off;
