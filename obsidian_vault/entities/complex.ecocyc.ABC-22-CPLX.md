---
entity_id: "complex.ecocyc.ABC-22-CPLX"
entity_type: "complex"
name: "oligopeptide ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-22-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# oligopeptide ABC transporter

`complex.ecocyc.ABC-22-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-22-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AFH6|protein.P0AFH6]], [[protein.P76027|protein.P76027]], [[protein.P77737|protein.P77737]], [[protein.P0AFH2|protein.P0AFH2]], [[protein.P23843|protein.P23843]]

## Enriched Summary

OppABCDF is a high affinity oligopeptide transporter that is a member of the ATP-binding cassette (ABC) superfamily of transporters. oppBC and oppDF encode two ATP binding subunits and two integral membrane proteins respectively, of an ABC transport system (see ) that interacts with either of two periplasmic peptide binding proteins, OppA - with a preference for positively charged tripeptides and tetrapeptides and MppA - which has affinity for murein tripeptides . OppABCDF contributes to the import of exogenous glutathione and is the main transporter for reduced glutathione . Orthologous systems have been extensively characterized in Salmonella typhimurium (see for example ). The novel peptide antibiotic, GE8112, which inhibits initiation of protein synthesis is an (illicit) substrate of the Opp ABC transporter . OppABCDF is a high affinity oligopeptide transporter that is a member of the ATP-binding cassette (ABC) superfamily of transporters. oppBC and oppDF encode two ATP binding subunits and two integral membrane proteins respectively, of an ABC transport system (see ) that interacts with either of two periplasmic peptide binding proteins, OppA - with a preference for positively charged tripeptides and tetrapeptides and MppA - which has affinity for murein tripeptides...

## Biological Role

Catalyzes 3.6.3.23-RXN (reaction.ecocyc.3.6.3.23-RXN), RXN0-11 (reaction.ecocyc.RXN0-11).

## Annotation

OppABCDF is a high affinity oligopeptide transporter that is a member of the ATP-binding cassette (ABC) superfamily of transporters. oppBC and oppDF encode two ATP binding subunits and two integral membrane proteins respectively, of an ABC transport system (see ) that interacts with either of two periplasmic peptide binding proteins, OppA - with a preference for positively charged tripeptides and tetrapeptides and MppA - which has affinity for murein tripeptides . OppABCDF contributes to the import of exogenous glutathione and is the main transporter for reduced glutathione . Orthologous systems have been extensively characterized in Salmonella typhimurium (see for example ). The novel peptide antibiotic, GE8112, which inhibits initiation of protein synthesis is an (illicit) substrate of the Opp ABC transporter .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.3.6.3.23-RXN|reaction.ecocyc.3.6.3.23-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-11|reaction.ecocyc.RXN0-11]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (5)

- `is_component_of` <-- [[protein.P0AFH2|protein.P0AFH2]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AFH6|protein.P0AFH6]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P23843|protein.P23843]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P76027|protein.P76027]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P77737|protein.P77737]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:ABC-22-CPLX`
- `QSPROTEOME:QS00176169`

## Notes

1*protein.P0AFH6|1*protein.P76027|1*protein.P77737|1*protein.P0AFH2|1*protein.P23843
