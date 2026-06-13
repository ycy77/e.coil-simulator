---
entity_id: "protein.P25714"
entity_type: "protein"
name: "yidC"
source_database: "UniProt"
source_id: "P25714"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11821429, ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:11821429, ECO:0000269|PubMed:16079137}. Note=Predominantly localized at cell poles at all stages of cell growth."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yidC b3705 JW3683"
---

# yidC

`protein.P25714`

## Static

- Type: `protein`
- Source: `UniProt:P25714`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11821429, ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:11821429, ECO:0000269|PubMed:16079137}. Note=Predominantly localized at cell poles at all stages of cell growth.

## Enriched Summary

FUNCTION: Inner membrane protein required for the insertion and/or proper folding and/or complex formation of integral inner membrane proteins. Involved in integration of membrane proteins that insert dependently and independently of the Sec translocase complex, as well as at least 2 lipoproteins. Its own insertion requires SRP and is Sec translocase-dependent. Essential for the integration of Sec-dependent subunit a of the F(0)ATP synthase, FtsQ and SecE proteins and for Sec-independent subunit c of the F(0)ATP synthase, M13 phage procoat and the N-terminus of leader peptidase Lep. Probably interacts directly with Sec-independent substrates. Sec-dependent protein FtsQ interacts first with SecY then subsequently with YidC. Sec-dependent LacY and MalF require YidC to acquire tertiary structure and stability, a chaperone-like function, but not for membrane insertion. Stable maltose transport copmplex formation (MalFGK(2)) also requires YidC. Partially complements a Streptococcus mutans yidC2 disruption mutant. {ECO:0000269|PubMed:10675323, ECO:0000269|PubMed:10949305, ECO:0000269|PubMed:12724529, ECO:0000269|PubMed:12950181, ECO:0000269|PubMed:15067017, ECO:0000269|PubMed:15140892, ECO:0000269|PubMed:17073462, ECO:0000269|PubMed:18456666}. YidC mediates membrane insertion/assembly of inner membrane proteins...

## Biological Role

Component of Sec Holo-Translocon (complex.ecocyc.SEC-SECRETION-CPLX).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Inner membrane protein required for the insertion and/or proper folding and/or complex formation of integral inner membrane proteins. Involved in integration of membrane proteins that insert dependently and independently of the Sec translocase complex, as well as at least 2 lipoproteins. Its own insertion requires SRP and is Sec translocase-dependent. Essential for the integration of Sec-dependent subunit a of the F(0)ATP synthase, FtsQ and SecE proteins and for Sec-independent subunit c of the F(0)ATP synthase, M13 phage procoat and the N-terminus of leader peptidase Lep. Probably interacts directly with Sec-independent substrates. Sec-dependent protein FtsQ interacts first with SecY then subsequently with YidC. Sec-dependent LacY and MalF require YidC to acquire tertiary structure and stability, a chaperone-like function, but not for membrane insertion. Stable maltose transport copmplex formation (MalFGK(2)) also requires YidC. Partially complements a Streptococcus mutans yidC2 disruption mutant. {ECO:0000269|PubMed:10675323, ECO:0000269|PubMed:10949305, ECO:0000269|PubMed:12724529, ECO:0000269|PubMed:12950181, ECO:0000269|PubMed:15067017, ECO:0000269|PubMed:15140892, ECO:0000269|PubMed:17073462, ECO:0000269|PubMed:18456666}.

## Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.SEC-SECRETION-CPLX|complex.ecocyc.SEC-SECRETION-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3705|gene.b3705]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25714`
- `KEGG:ecj:JW3683;eco:b3705;ecoc:C3026_20090;`
- `GeneID:75173922;948214;`
- `GO:GO:0005886; GO:0006457; GO:0016020; GO:0031522; GO:0032977; GO:0043952; GO:0051205; GO:0065003`

## Notes

Membrane protein insertase YidC (Foldase YidC) (Inner membrane protein YidC) (Membrane integrase YidC) (Oxa1Ec)
