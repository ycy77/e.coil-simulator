---
entity_id: "protein.P0A6K3"
entity_type: "protein"
name: "def"
source_database: "UniProt"
source_id: "P0A6K3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "def fms b3287 JW3248"
---

# def

`protein.P0A6K3`

## Static

- Type: `protein`
- Source: `UniProt:P0A6K3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Removes the formyl group from the N-terminal Met of newly synthesized proteins (PubMed:7896716). Requires at least a dipeptide for an efficient rate of reaction. N-terminal L-methionine is a prerequisite for activity but the enzyme has broad specificity at other positions. {ECO:0000269|PubMed:7896716, ECO:0000269|PubMed:9610360, ECO:0000305|PubMed:8244948}. Peptide deformylase (PDF) releases the formyl group from the amino terminal methionine residue of most nascent proteins . It interacts directly with the ribosome at the ribosomal exit tunnel and competes with EG10570-MONOMER (MAP) for the same site . PDF is essential in E. coli . A proteome-wide analysis of N termini in the presence and after depletion of PDF has been performed . The specific physiological function of the N-terminal formylated methionine residue (fMet) in proteins is uncertain. It was shown that N-terminal fMet can act as a co-translational degradation signal . Using the PDF inhibitor, CPD0-1358, and time-resolved analyses of proteome and translatome revealed that disruption of PDF function induces different stages of cellular responses with protein misfolding and membrane stress responses occurring prior to effects on metabolic pathways...

## Biological Role

Catalyzes 3.5.1.88-RXN (reaction.ecocyc.3.5.1.88-RXN). Bound by Fe2+ (molecule.C14818).

## Annotation

FUNCTION: Removes the formyl group from the N-terminal Met of newly synthesized proteins (PubMed:7896716). Requires at least a dipeptide for an efficient rate of reaction. N-terminal L-methionine is a prerequisite for activity but the enzyme has broad specificity at other positions. {ECO:0000269|PubMed:7896716, ECO:0000269|PubMed:9610360, ECO:0000305|PubMed:8244948}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.5.1.88-RXN|reaction.ecocyc.3.5.1.88-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3287|gene.b3287]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6K3`
- `KEGG:ecj:JW3248;eco:b3287;ecoc:C3026_17870;`
- `GeneID:86862316;89518132;947780;`
- `GO:GO:0005829; GO:0006412; GO:0008198; GO:0008270; GO:0016787; GO:0042586; GO:0043022`
- `EC:3.5.1.88`

## Notes

Peptide deformylase (PDF) (EC 3.5.1.88) (Polypeptide deformylase)
