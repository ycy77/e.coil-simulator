---
entity_id: "protein.P0AC98"
entity_type: "protein"
name: "satP"
source_database: "UniProt"
source_id: "P0AC98"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "satP yaaH b0010 JW0009"
---

# satP

`protein.P0AC98`

## Static

- Type: `protein`
- Source: `UniProt:P0AC98`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Uptake of acetate and succinate. Transport is energetically dependent on the protonmotive force. {ECO:0000269|PubMed:23844911}. SatP is an acetate:proton symporter that is implicated in acetate homeostasis when E. coli K-12 is grown aerobically at high glucose concentrations; under these conditons, SatP is active in acetate transport at the exponential growth stage whereas the acetate permease YJCG-MONOMER "ActP" is more active at the entry to stationary phase; SatP is implicated in acetate uptake when E. coli is grown with acetic acid as the sole carbon and energy source . In transport assays, succinate is a competitive inhibitor for acetate uptake by YaaH; the absence of YaaH is associated with an increase in the amount of succinate found (at the 10 hour timepoint) in the culture supernatant of cells grown aerobically with glucose; this increase appears consistent with a decrease in succinate uptake . SatP contributes to the residual succinate uptake seen in mutant strains lacking the major aerobic succinate transporters DctA and DauA . SatP is predicted to have 6 membrane spanning alpha-helices with the C-terminus located in the cytoplasm . SatP is predicted to form a hexameric ring structure with strong similarity to the proton-gated urea channel, Ure1, from Helicobacter pylori...

## Biological Role

Catalyzes succinate:proton symport (reaction.ecocyc.TRANS-RXN-121), acetate:proton symport (reaction.ecocyc.TRANS-RXN0-571). Transports Acetate (molecule.C00033), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Uptake of acetate and succinate. Transport is energetically dependent on the protonmotive force. {ECO:0000269|PubMed:23844911}.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-121|reaction.ecocyc.TRANS-RXN-121]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-571|reaction.ecocyc.TRANS-RXN0-571]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b0010|gene.b0010]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC98`
- `KEGG:ecj:JW0009;eco:b0010;ecoc:C3026_00055;`
- `GeneID:86862527;93777432;944792;`
- `GO:GO:0005886; GO:0015360; GO:0035433; GO:0071422`

## Notes

Succinate-acetate/proton symporter SatP (Succinate-acetate transporter protein)
