---
entity_id: "protein.P0C0L7"
entity_type: "protein"
name: "proP"
source_database: "UniProt"
source_id: "P0C0L7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:10026245, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "proP b4111 JW4072"
---

# proP

`protein.P0C0L7`

## Static

- Type: `protein`
- Source: `UniProt:P0C0L7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:10026245, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Proton symporter that senses osmotic shifts and responds by importing osmolytes such as proline, glycine betaine, stachydrine, pipecolic acid, ectoine and taurine. It is both an osmosensor and an osmoregulator which is available to participate early in the bacterial osmoregulatory response. {ECO:0000269|PubMed:10026245, ECO:0000269|PubMed:3082857, ECO:0000269|PubMed:8421314}. ProP is an osmosensing transporter which mediates the uptake of zwitterionic osmolytes such as proline and glycine betaine; ProP function protects cells from dehydration under conditions of hyperosmotic stress. The proP locus was first defined in E. coli K-12 (strain RM2 ΔputPA) by mutations which eliminate an inducible proline uptake activity and increase resistance to the toxic proline analaog, 3,4-dehydroproline . ProP mediated proline uptake is induced and stimulated by osmotic stress ; ProP has similar affinity for proline and glycine betaine . ProP catalyses active proline uptake in cytoplasmic membrane vesicles; ProP activity measured in whole cells is eliminated by the uncoupling agent CCCP and the respiration inhibitor KCN . ProP functions as a proline:H+ symporter ; purified ProP reconstituted in liposomes catalyses the active accumulation of proline, this activity requires both membrane potential and an osmotic upshift and maximum uptake occurs in the presence of a pH downshift...

## Biological Role

Component of osmolyte:H+ symporter ProP (complex.ecocyc.CPLX0-7642).

## Annotation

FUNCTION: Proton symporter that senses osmotic shifts and responds by importing osmolytes such as proline, glycine betaine, stachydrine, pipecolic acid, ectoine and taurine. It is both an osmosensor and an osmoregulator which is available to participate early in the bacterial osmoregulatory response. {ECO:0000269|PubMed:10026245, ECO:0000269|PubMed:3082857, ECO:0000269|PubMed:8421314}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7642|complex.ecocyc.CPLX0-7642]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4111|gene.b4111]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C0L7`
- `KEGG:ecj:JW4072;eco:b4111;ecoc:C3026_22210;`
- `GeneID:948626;`
- `GO:GO:0005297; GO:0005886; GO:0006865; GO:0007231; GO:0015294; GO:0031460; GO:0042803; GO:0071474; GO:0071475; GO:1905647`

## Notes

Proline/betaine transporter (Proline porter II) (PPII)
