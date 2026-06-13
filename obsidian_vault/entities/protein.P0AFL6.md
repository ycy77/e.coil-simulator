---
entity_id: "protein.P0AFL6"
entity_type: "protein"
name: "ppx"
source_database: "UniProt"
source_id: "P0AFL6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000305|PubMed:8380170}; Peripheral membrane protein {ECO:0000305|PubMed:8380170}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ppx b2502 JW2487"
---

# ppx

`protein.P0AFL6`

## Static

- Type: `protein`
- Source: `UniProt:P0AFL6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000305|PubMed:8380170}; Peripheral membrane protein {ECO:0000305|PubMed:8380170}.

## Enriched Summary

FUNCTION: Degradation of inorganic polyphosphates (polyP). Releases orthophosphate processively from the ends of the polyP chain. Has a strong preference for long-chain polyphosphates and has only weak affinity for smaller size polyP of about 15 residues. {ECO:0000269|PubMed:16905100, ECO:0000269|PubMed:8380170, ECO:0000269|PubMed:9143103}. Exopolyphosphatase (PPX) degrades inorganic polyphosphates (polyP). It has a strong preference for long-chain polyphosphates; activity decreases with smaller size polyP of about 15 residues. PPX acts on the ends of the polyP chain, removing orthophosphate processively . Steady-state levels of polyP are dependent on the level of PPX in the cell . pppGpp and ppGpp strongly inhibit PPX activity while also acting as a substrate; however, GppA is the major source of pppGppase activity in the cell . PPX activity is redox-regulated; the enzyme is highly sensitive to inactivation by oxidation. Thus, oxidative stress conditions lead to accumulation of poly(P), which acts as a global chaperone . The N terminus of PPX contains the active site and belongs to the ASKHA (acetate and sugar kinases, Hsp70, actin) phosphotranferase superfamily, while the C terminus binds polyphosphate. The halves can be expressed separately and combined to form a functional enzyme . Crystal structures of the enzyme have been solved at 1.9 Å and 2.2 Å (using E...

## Biological Role

Catalyzes guanosine 3'-diphosphate 5'-triphosphate 5'-phosphohydrolase (reaction.R03409). Component of exopolyphosphatase (complex.ecocyc.PPX-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Degradation of inorganic polyphosphates (polyP). Releases orthophosphate processively from the ends of the polyP chain. Has a strong preference for long-chain polyphosphates and has only weak affinity for smaller size polyP of about 15 residues. {ECO:0000269|PubMed:16905100, ECO:0000269|PubMed:8380170, ECO:0000269|PubMed:9143103}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R03409|reaction.R03409]] `KEGG` `database` - via EC:3.6.1.11
- `is_component_of` --> [[complex.ecocyc.PPX-CPLX|complex.ecocyc.PPX-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2502|gene.b2502]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFL6`
- `KEGG:ecj:JW2487;eco:b2502;ecoc:C3026_13875;`
- `GeneID:93774634;946970;`
- `GO:GO:0004309; GO:0005886; GO:0006798; GO:0042802; GO:0042803; GO:0097216`
- `EC:3.6.1.11`

## Notes

Exopolyphosphatase (ExopolyPase) (EC 3.6.1.11) (Metaphosphatase)
