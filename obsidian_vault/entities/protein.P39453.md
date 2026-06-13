---
entity_id: "protein.P39453"
entity_type: "protein"
name: "torS"
source_database: "UniProt"
source_id: "P39453"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "torS yccI b0993 JW5135"
---

# torS

`protein.P39453`

## Static

- Type: `protein`
- Source: `UniProt:P39453`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system TorS/TorR involved in the anaerobic utilization of trimethylamine-N-oxide (TMAO). Detects the presence of TMAO in the medium and, in response, activates TorR via a four-step phosphorelay. When TMAO is removed, TorS can dephosphorylate TorR, probably by a reverse phosphorelay involving His-860 and Asp-733. TorS is the histidine kinase of a multi component regulatory system which induces expression of the torCAD operon encoding the trimethylamine-N-oxide (TMAO) respiratory system of E. coli. TorS is required for torCAD operon expression . TorS contains three phosphorylation sites and is an unorthodox sensor kinase; the protein contains two predicted transmembrane regions, an N-terminal detector or sensor region, a transmitter domain with a histidine phosphorylation site (H443) and an ATP binding motif, a receiver domain with an aspartate phosphorylation site (D723), and a C-terminal alternative transmitter domain with a phosphorylation site (H850) . All three phosphorylation sites are required for transphosphorylation of TorR in vitro; H443 is required for autophosphorylation of TorS and is likely the initial site of phosphorylation; D723 and H850 are required for transphosphorylation of TorR; TorR is thought to be transphosphorylated through a four-step phosphorelay TorS(H850) → TorS(D723) → TorS(H850) → TorR(D53)...

## Biological Role

Component of TorTS signaling complex (complex.ecocyc.CPLX0-11302), TorS-N-phospho-L-histidine-443 (complex.ecocyc.CPLX0-8265), TorS-phospho-L-aspartate-723 (complex.ecocyc.CPLX0-8267), TorS-N-phospho-L-histidine-850 (complex.ecocyc.CPLX0-8268), sensor histidine kinase TorS (complex.ecocyc.TORS-CPLX).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system TorS/TorR involved in the anaerobic utilization of trimethylamine-N-oxide (TMAO). Detects the presence of TMAO in the medium and, in response, activates TorR via a four-step phosphorelay. When TMAO is removed, TorS can dephosphorylate TorR, probably by a reverse phosphorelay involving His-860 and Asp-733.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-11302|complex.ecocyc.CPLX0-11302]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8265|complex.ecocyc.CPLX0-8265]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8267|complex.ecocyc.CPLX0-8267]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8268|complex.ecocyc.CPLX0-8268]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.TORS-CPLX|complex.ecocyc.TORS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0993|gene.b0993]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39453`
- `KEGG:ecj:JW5135;eco:b0993;`
- `GeneID:945595;`
- `GO:GO:0000155; GO:0000160; GO:0004721; GO:0005524; GO:0005886; GO:0009061; GO:0042802; GO:0042803`
- `EC:2.7.13.3`

## Notes

Sensor protein TorS (EC 2.7.13.3)
