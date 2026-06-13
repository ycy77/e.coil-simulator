---
entity_id: "protein.P0AB18"
entity_type: "protein"
name: "tusE"
source_database: "UniProt"
source_id: "P0AB18"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tusE yccK b0969 JW0952"
---

# tusE

`protein.P0AB18`

## Static

- Type: `protein`
- Source: `UniProt:P0AB18`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of a sulfur-relay system required for 2-thiolation of 5-methylaminomethyl-2-thiouridine (mnm(5)s(2)U) at tRNA wobble positions. Could accept sulfur from TusD. {ECO:0000269|PubMed:16387657}. TusE functions as a sulfur mediator during synthesis of 2-thiouridine of the modified wobble base mnm5s2U in tRNA. TusE directly interacts with both the TusBCD complex and the MnmA-tRNA complex, but not with tRNA itself . TusE accepts the sulfur from the CPLX-3942 and transfers it to Cys199 of MnmA . 2-thiouridine formation in vitro is greatly enhanced in the presence of TusE. TusE is labeled by 35S sulfur during 2-thiouridine formation in vitro . A tusE deletion mutant lacks mnm5s2U, accumulates mnm5U and has a growth defect. The cysteine residue C108 is required for sulfur transfer . TusE: "tRNA 2-thiouridine synthesizing protein"

## Biological Role

Catalyzes RXN-22699 (reaction.ecocyc.RXN-22699).

## Enriched Pathways

- `eco04122` Sulfur relay system (KEGG)

## Annotation

FUNCTION: Part of a sulfur-relay system required for 2-thiolation of 5-methylaminomethyl-2-thiouridine (mnm(5)s(2)U) at tRNA wobble positions. Could accept sulfur from TusD. {ECO:0000269|PubMed:16387657}.

## Pathways

- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-22699|reaction.ecocyc.RXN-22699]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0969|gene.b0969]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB18`
- `KEGG:ecj:JW0952;eco:b0969;ecoc:C3026_05920;`
- `GeneID:93776445;945023;`
- `GO:GO:0002143; GO:0016740; GO:0097163; GO:1990228`
- `EC:2.8.1.-`

## Notes

Sulfurtransferase TusE (EC 2.8.1.-) (tRNA 2-thiouridine synthesizing protein E)
