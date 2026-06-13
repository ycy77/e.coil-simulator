---
entity_id: "gene.b1193"
entity_type: "gene"
name: "emtA"
source_database: "NCBI RefSeq"
source_id: "gene-b1193"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1193"
  - "emtA"
---

# emtA

`gene.b1193`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1193`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

emtA (gene.b1193) is a gene entity. It encodes emtA (protein.P0C960). Encoded protein function: FUNCTION: Murein-degrading enzyme. May play a role in recycling of muropeptides during cell elongation and/or cell division. Preferentially cleaves at a distance of more than two disaccharide units from the ends of the glycan chain. Prefers cross-linked murein in vivo. EcoCyc product frame: G6622-MONOMER. EcoCyc synonyms: ycgP, mltE, sltZ. Genomic coordinates: 1243180-1243791. EcoCyc protein note: emtA encodes a membrane bound lytic murein transglycosylase (EmtA or MltE) which cleaves the β-1 → 4 glycosidic bond between N-acetylglucosamine (GlcNAc) and N-acetylmuramic acid (MurNAc) residues of peptidoglycan with the concomitant formation of a 1,6-anhydro ring at the MurNAc residue. EmtA is a lipoprotein, predicted to reside in the outer membrane . EmtA degrades isolated murein glycan strands to release muropeptides with a 1,6-anhydroMurNAc terminus; EmtA has endotransglycosylase activity - it hydrolyses glycan strands in vitro to produce fragments with lengths of two and three disaccharide units but does not produce monomeric anhydrodisaccharide fragments; EmtA displays a preference for cross-linked murein; EmtA is unable to degrade purified murein sacculi in vitro . Purified EmtA (residues 17-203) cleaves Micrococcus luteus murein sacculi in vitro...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C960|protein.P0C960]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004006,ECOCYC:G6622,GeneID:945655`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1243180-1243791:+; feature_type=gene
