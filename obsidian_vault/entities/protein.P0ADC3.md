---
entity_id: "protein.P0ADC3"
entity_type: "protein"
name: "lolC"
source_database: "UniProt"
source_id: "P0ADC3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lolC ycfU b1116 JW5161"
---

# lolC

`protein.P0ADC3`

## Static

- Type: `protein`
- Source: `UniProt:P0ADC3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Part of an ATP-dependent transport system LolCDE responsible for the release of lipoproteins targeted to the outer membrane from the inner membrane. Such a release is dependent of the sorting-signal (absence of an Asp at position 2 of the mature lipoprotein) and of LolA. LolC is an inner membrane subunit of the LolCDE lipoprotein release complex . LolC contains 4 predicted transmembrane regions; a large loop region between the first and second transmembrane regions is located in the periplasm . The periplasmic domain of LolC contains structural features that underpin the mechanotransmission mechanism of the type VII ABC transporter, MACB "MacB" . The periplasmic domain of LolC contains a 'hook' (residues P167 - P179) and 'pad' (R163, Q181, R182) that mediate interaction with the lipopotein chaperone G6465-MONOMER LolA; the interaction between LolA and LolCDE occurs exclusively through LolC and is independent of nucleotide binding and hydrolysis; LolC discriminates between LolA and LolB (see also ).

## Biological Role

Component of lipoprotein release complex (complex.ecocyc.ABC-62-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of an ATP-dependent transport system LolCDE responsible for the release of lipoproteins targeted to the outer membrane from the inner membrane. Such a release is dependent of the sorting-signal (absence of an Asp at position 2 of the mature lipoprotein) and of LolA.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-62-CPLX|complex.ecocyc.ABC-62-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1116|gene.b1116]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADC3`
- `KEGG:ecj:JW5161;eco:b1116;`
- `GeneID:93776292;945673;`
- `GO:GO:0005886; GO:0030288; GO:0042953; GO:0043190; GO:0044874; GO:0089705; GO:0098797; GO:0140306`

## Notes

Lipoprotein-releasing system transmembrane protein LolC
