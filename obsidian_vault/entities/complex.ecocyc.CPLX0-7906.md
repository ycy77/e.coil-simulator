---
entity_id: "complex.ecocyc.CPLX0-7906"
entity_type: "complex"
name: "L-carnitine:γ-butyrobetaine antiporter"
source_database: "EcoCyc"
source_id: "CPLX0-7906"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# L-carnitine:γ-butyrobetaine antiporter

`complex.ecocyc.CPLX0-7906`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7906`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P31553|protein.P31553]]

## Enriched Summary

CaiT is an L-carnitine:γ-butyrobetaine antiporter. Expression of caiT from a plasmid increases methyl-L-carnitine transport into cells preloaded with L-carnitine or γ-butyrobetaine; purified CaiT, reconstituted in proteoliposomes catalyses L-carnitine counter exchange, L-carnitine:γ-butyrobetaine antiport, L-carnitine:crotonobetaine antiport and L-carnitine:D-carnitine antiport. CaiT is believed to exchange exogenous L-carnitine for the carnitine conversion product, γ-butyrobetaine, in vivo . CaiT is predicted to contain 12 transmembrane regions with the C and N-termini located in the cytoplasm . CaiT belongs to the Betaine/Carnitine/Choline Transport (BCCT) Family . CaiT is an L-carnitine:γ-butyrobetaine antiporter. Expression of caiT from a plasmid increases methyl-L-carnitine transport into cells preloaded with L-carnitine or γ-butyrobetaine; purified CaiT, reconstituted in proteoliposomes catalyses L-carnitine counter exchange, L-carnitine:γ-butyrobetaine antiport, L-carnitine:crotonobetaine antiport and L-carnitine:D-carnitine antiport. CaiT is believed to exchange exogenous L-carnitine for the carnitine conversion product, γ-butyrobetaine, in vivo . CaiT is predicted to contain 12 transmembrane regions with the C and N-termini located in the cytoplasm . CaiT belongs to the Betaine/Carnitine/Choline Transport (BCCT) Family .

## Biological Role

Catalyzes L-carnitine:γ-butyrobetaine antiport (reaction.ecocyc.TRANS-RXN-100). Transports 4-Trimethylammoniobutanoate (molecule.C01181), L-carnitine (molecule.ecocyc.CARNITINE).

## Annotation

CaiT is an L-carnitine:γ-butyrobetaine antiporter. Expression of caiT from a plasmid increases methyl-L-carnitine transport into cells preloaded with L-carnitine or γ-butyrobetaine; purified CaiT, reconstituted in proteoliposomes catalyses L-carnitine counter exchange, L-carnitine:γ-butyrobetaine antiport, L-carnitine:crotonobetaine antiport and L-carnitine:D-carnitine antiport. CaiT is believed to exchange exogenous L-carnitine for the carnitine conversion product, γ-butyrobetaine, in vivo . CaiT is predicted to contain 12 transmembrane regions with the C and N-termini located in the cytoplasm . CaiT belongs to the Betaine/Carnitine/Choline Transport (BCCT) Family .

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-100|reaction.ecocyc.TRANS-RXN-100]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C01181|molecule.C01181]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CARNITINE|molecule.ecocyc.CARNITINE]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P31553|protein.P31553]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3

## External IDs

- `EcoCyc:CPLX0-7906`
- `QSPROTEOME:QS00183113`

## Notes

3*protein.P31553
