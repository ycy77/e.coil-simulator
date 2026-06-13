---
entity_id: "protein.P0A8V0"
entity_type: "protein"
name: "rbn"
source_database: "UniProt"
source_id: "P0A8V0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rbn elaC rnz b2268 JW2263"
---

# rbn

`protein.P0A8V0`

## Static

- Type: `protein`
- Source: `UniProt:P0A8V0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Zinc phosphodiesterase, which has both exoribonuclease and endoribonuclease activities, depending on the nature of the substrate and of the added divalent cation, and on its 3'-terminal structure. Can process the 3' termini of both CCA-less and CCA-containing tRNA precursors. CCA-less tRNAs are cleaved endonucleolytically after the discriminator base, whereas residues following the CCA sequence can be removed exonucleolytically or endonucleolytically in CCA-containing molecules. Does not remove the CCA sequence. May also be involved in the degradation of mRNAs. In vitro, hydrolyzes bis(p-nitrophenyl)phosphate and thymidine-5'-p-nitrophenyl phosphate. {ECO:0000269|PubMed:12029081, ECO:0000269|PubMed:15764599, ECO:0000269|PubMed:16629673, ECO:0000269|PubMed:19366704, ECO:0000269|PubMed:20489203}.

## Biological Role

Component of ribonuclease BN (complex.ecocyc.CPLX0-3601).

## Annotation

FUNCTION: Zinc phosphodiesterase, which has both exoribonuclease and endoribonuclease activities, depending on the nature of the substrate and of the added divalent cation, and on its 3'-terminal structure. Can process the 3' termini of both CCA-less and CCA-containing tRNA precursors. CCA-less tRNAs are cleaved endonucleolytically after the discriminator base, whereas residues following the CCA sequence can be removed exonucleolytically or endonucleolytically in CCA-containing molecules. Does not remove the CCA sequence. May also be involved in the degradation of mRNAs. In vitro, hydrolyzes bis(p-nitrophenyl)phosphate and thymidine-5'-p-nitrophenyl phosphate. {ECO:0000269|PubMed:12029081, ECO:0000269|PubMed:15764599, ECO:0000269|PubMed:16629673, ECO:0000269|PubMed:19366704, ECO:0000269|PubMed:20489203}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3601|complex.ecocyc.CPLX0-3601]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2268|gene.b2268]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8V0`
- `KEGG:ecj:JW2263;eco:b2268;ecoc:C3026_12665;`
- `GeneID:946760;`
- `GO:GO:0004518; GO:0004532; GO:0008033; GO:0008270; GO:0016891; GO:0016896; GO:0042781; GO:0042803; GO:0046872`
- `EC:3.1.-.-`

## Notes

Ribonuclease BN (RNase BN) (EC 3.1.-.-) (Ribonuclease Z homolog) (RNase Z homolog)
