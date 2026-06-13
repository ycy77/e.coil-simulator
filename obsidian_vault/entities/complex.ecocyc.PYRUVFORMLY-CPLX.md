---
entity_id: "complex.ecocyc.PYRUVFORMLY-CPLX"
entity_type: "complex"
name: "activated pyruvate-formate lyase"
source_database: "EcoCyc"
source_id: "PYRUVFORMLY-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# activated pyruvate-formate lyase

`complex.ecocyc.PYRUVFORMLY-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PYRUVFORMLY-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN
- Complex type: `regulatory`
- Components: [[protein.P09373|protein.P09373]]

## Enriched Summary

Escherichia coli pyruvate-formate lyase (PflB) is a central enzyme of anaerobic metabolism. It catalyzes the coenzyme A-dependent, non-oxidative cleavage of pyruvate to acetyl-CoA and formate in anaerobically growing cells (see pathway FERMENTATION-PWY). Under anaerobic conditions, induction of transcription of pflB involves CPLX0-7797 and the PHOSPHO-ARCA and ARCB-CPLX regulatory proteins . At the post-translational level the enzyme is regulated by activation . Activation of the inactive enzyme is catalyzed by the same PFLACTENZ-MONOMER that also activates KETOBUTFORMLY-INACT-MONOMER . This activation process requires reduced flavodoxin that is generated via a coenzyme A-acylating PYRUFLAVREDUCT-MONOMER, or FLAVONADPREDUCT-MONOMER . Activation introduces a free radical into the enzyme (see below). PflB utilizes a "ping-pong" mechanism that proceeds via two half-reactions. The enzyme is also active with 2-oxobutanoate as substrate, but pyruvate is the preferred substrate . An active site Gly734 radical is used to reversibly cleave the C1-C2 bond of pyruvate. This radical is also thought to generate thiyl radicals at active site residues Cys418 and Cys419 for homolytic substrate cleavage . The relatively stable glycyl radical is sensitive to OXYGEN-MOLECULE and essential for catalysis...

## Biological Role

Catalyzes KETOBUTFORMLY-RXN (reaction.ecocyc.KETOBUTFORMLY-RXN), PYRUVFORMLY-RXN (reaction.ecocyc.PYRUVFORMLY-RXN). Component of PFL-GrcA complex (complex.ecocyc.CPLX0-9871).

## Annotation

Escherichia coli pyruvate-formate lyase (PflB) is a central enzyme of anaerobic metabolism. It catalyzes the coenzyme A-dependent, non-oxidative cleavage of pyruvate to acetyl-CoA and formate in anaerobically growing cells (see pathway FERMENTATION-PWY). Under anaerobic conditions, induction of transcription of pflB involves CPLX0-7797 and the PHOSPHO-ARCA and ARCB-CPLX regulatory proteins . At the post-translational level the enzyme is regulated by activation . Activation of the inactive enzyme is catalyzed by the same PFLACTENZ-MONOMER that also activates KETOBUTFORMLY-INACT-MONOMER . This activation process requires reduced flavodoxin that is generated via a coenzyme A-acylating PYRUFLAVREDUCT-MONOMER, or FLAVONADPREDUCT-MONOMER . Activation introduces a free radical into the enzyme (see below). PflB utilizes a "ping-pong" mechanism that proceeds via two half-reactions. The enzyme is also active with 2-oxobutanoate as substrate, but pyruvate is the preferred substrate . An active site Gly734 radical is used to reversibly cleave the C1-C2 bond of pyruvate. This radical is also thought to generate thiyl radicals at active site residues Cys418 and Cys419 for homolytic substrate cleavage . The relatively stable glycyl radical is sensitive to OXYGEN-MOLECULE and essential for catalysis . Destruction of the glycyl radical by oxygen results in cleavage of the 85 kDa polypeptide to 83 kDa and a 3 kDa fragment and consequent inactivation of the enzyme . The damaged PFL enzyme may be reactivated by the "spare part" protein EG11784-MONOMER . This small (14-kDa) protein forms a complex with the damaged PFL dimer and displaces the C-terminal glycyl radical domain, restoring the catalytic function of PflB . The enzyme can also be deactivated enzymatically. It has been suggested th

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.KETOBUTFORMLY-RXN|reaction.ecocyc.KETOBUTFORMLY-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PYRUVFORMLY-RXN|reaction.ecocyc.PYRUVFORMLY-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-9871|complex.ecocyc.CPLX0-9871]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P09373|protein.P09373]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PYRUVFORMLY-CPLX`

## Notes

2*protein.P09373
