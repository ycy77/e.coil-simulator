---
entity_id: "complex.ecocyc.BRANCHED-CHAINAMINOTRANSFER-CPLX"
entity_type: "complex"
name: "branched-chain-amino-acid aminotransferase"
source_database: "EcoCyc"
source_id: "BRANCHED-CHAINAMINOTRANSFER-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "BCAT"
  - "transaminase B"
---

# branched-chain-amino-acid aminotransferase

`complex.ecocyc.BRANCHED-CHAINAMINOTRANSFER-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:BRANCHED-CHAINAMINOTRANSFER-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AB80|protein.P0AB80]]

## Enriched Summary

Branched-chain amino acid aminotransferase (IlvE) is a multifunctional enzyme that carries out the final step in valine, leucine and isoleucine biosyntheses. IlvE catalyzes three reversible transamination reactions, each of which generates α-ketoglutarate and one of three aliphatic amino acids . It can also catalyze transamination to produce phenylalanine and tyrosine, though it is much less efficient in this role . IlvE forms a hexamer consisting of a dimer of trimers . A crystal structure of IlvE to 2.5 Å resolution confirms this hexameric configuration, as well as showing that each IlvE monomer consists of two domains, with the pyridoxal group at the domain interface . Structures containing glutamate and glutarate, to 1.82 Å and 2.15 Å resolution, respectively, have been used to examine substrate binding . Branched-chain amino acid aminotransferase (IlvE) is a multifunctional enzyme that carries out the final step in valine, leucine and isoleucine biosyntheses. IlvE catalyzes three reversible transamination reactions, each of which generates α-ketoglutarate and one of three aliphatic amino acids . It can also catalyze transamination to produce phenylalanine and tyrosine, though it is much less efficient in this role . IlvE forms a hexamer consisting of a dimer of trimers . A crystal structure of IlvE to 2...

## Biological Role

Catalyzes BRANCHED-CHAINAMINOTRANSFERILEU-RXN (reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERILEU-RXN), BRANCHED-CHAINAMINOTRANSFERLEU-RXN (reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN), BRANCHED-CHAINAMINOTRANSFERVAL-RXN (reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERVAL-RXN), RXN-10814 (reaction.ecocyc.RXN-10814). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

Branched-chain amino acid aminotransferase (IlvE) is a multifunctional enzyme that carries out the final step in valine, leucine and isoleucine biosyntheses. IlvE catalyzes three reversible transamination reactions, each of which generates α-ketoglutarate and one of three aliphatic amino acids . It can also catalyze transamination to produce phenylalanine and tyrosine, though it is much less efficient in this role . IlvE forms a hexamer consisting of a dimer of trimers . A crystal structure of IlvE to 2.5 Å resolution confirms this hexameric configuration, as well as showing that each IlvE monomer consists of two domains, with the pyridoxal group at the domain interface . Structures containing glutamate and glutarate, to 1.82 Å and 2.15 Å resolution, respectively, have been used to examine substrate binding .

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERILEU-RXN|reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERILEU-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN|reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERVAL-RXN|reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERVAL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-10814|reaction.ecocyc.RXN-10814]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AB80|protein.P0AB80]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:BRANCHED-CHAINAMINOTRANSFER-CPLX`
- `QSPROTEOME:QS00181709`

## Notes

6*protein.P0AB80
