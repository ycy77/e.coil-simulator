---
entity_id: "complex.ecocyc.CPLX0-7564"
entity_type: "complex"
name: "4-hydroxy-3-methylbut-2-enyl diphosphate reductase"
source_database: "EcoCyc"
source_id: "CPLX0-7564"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 4-hydroxy-3-methylbut-2-enyl diphosphate reductase

`complex.ecocyc.CPLX0-7564`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7564`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P62623|protein.P62623]]

## Enriched Summary

4-hydroxy-3-methylbut-2-enyl diphosphate reductase (IspH) is involved in what is effectively the final step of the methylerythritol phosphate (MEP) pathway, generating the two pathway products isopentyl pyrophosphate (IPP) and dimethylallyl pyrophosphate (DMAPP). IspH catalyzes the reductive dehydroxylation 4-hydroxy-3-methylbut-2-enyl diphosphate into a 5-6:1 mix of IPP and DMAPP . This ratio is subsequently adjusted to 3:7 by another pathway enzyme, IPPISOM-MONOMER . In vitro reconstitution of IspH functions requires the presence of a reducing system, such as flavodoxin and flavodoxin reductase, or photoreduced deazaflavin . Notably, Flavodoxin flavodoxin is required for proper MEP pathway function in vivo . IspH was reported to have either a [4Fe-4S] or a [3Fe-4S] cluster that is critical for its catalytic activity . Later structural studies confirmed the presence of a [4Fe-4S] cluster with a unique fourth iron site, which is coordinated (in substrate-free protein) to three water molecules and three bridging sulfur atoms of the cluster . ispH mutants are sensitive to penicillin and prone to cell lysis . IspH also appears to be involved in the stringent response . The crystal structure of IspH has been determined in complex with substrate, converted substrate, products and PP(i)...

## Biological Role

Catalyzes RXN-24043 (reaction.ecocyc.RXN-24043), RXN-24044 (reaction.ecocyc.RXN-24044). Bound by FAD (molecule.C00016), Cobalt ion (molecule.C00175), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

4-hydroxy-3-methylbut-2-enyl diphosphate reductase (IspH) is involved in what is effectively the final step of the methylerythritol phosphate (MEP) pathway, generating the two pathway products isopentyl pyrophosphate (IPP) and dimethylallyl pyrophosphate (DMAPP). IspH catalyzes the reductive dehydroxylation 4-hydroxy-3-methylbut-2-enyl diphosphate into a 5-6:1 mix of IPP and DMAPP . This ratio is subsequently adjusted to 3:7 by another pathway enzyme, IPPISOM-MONOMER . In vitro reconstitution of IspH functions requires the presence of a reducing system, such as flavodoxin and flavodoxin reductase, or photoreduced deazaflavin . Notably, Flavodoxin flavodoxin is required for proper MEP pathway function in vivo . IspH was reported to have either a [4Fe-4S] or a [3Fe-4S] cluster that is critical for its catalytic activity . Later structural studies confirmed the presence of a [4Fe-4S] cluster with a unique fourth iron site, which is coordinated (in substrate-free protein) to three water molecules and three bridging sulfur atoms of the cluster . ispH mutants are sensitive to penicillin and prone to cell lysis . IspH also appears to be involved in the stringent response . The crystal structure of IspH has been determined in complex with substrate, converted substrate, products and PP(i). The protein resembles a three-leaf clover and is composed of three structurally similar domains with no detectable sequence similarity. The active site is buried in a hydrophobic cavity embedded between the three domains. Each domain contributes on of the three cysteines that coordinate the [4Fe-4S] cluster . Crystal structures of IspH mutant proteins show an alternate substrate conformation as compared to wild-type proteins . Much as ispG mutants are deficient in activation of human Vγ9Vδ2 T

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-24043|reaction.ecocyc.RXN-24043]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-24044|reaction.ecocyc.RXN-24044]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P62623|protein.P62623]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7564`
- `QSPROTEOME:QS00181849`

## Notes

2*protein.P62623
