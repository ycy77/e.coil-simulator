---
entity_id: "gene.b1780"
entity_type: "gene"
name: "yeaD"
source_database: "NCBI RefSeq"
source_id: "gene-b1780"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1780"
  - "yeaD"
---

# yeaD

`gene.b1780`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1780`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeaD (gene.b1780) is a gene entity. It encodes yeaD (protein.P39173). Encoded protein function: Putative glucose-6-phosphate 1-epimerase (EC 5.1.3.15) (Putative D-hexose-6-phosphate mutarotase) (Unknown protein from 2D-page spots T26/PR37) EcoCyc product frame: G6966-MONOMER. EcoCyc synonyms: yzzQ. Genomic coordinates: 1863850-1864734. EcoCyc protein note: Overexpression of yeaD slightly increases fitness as well as resistance to the antibiotic aztreonam and suppresses the essentiality of EG12691-MONOMER "lapB", which encodes a protein involved in lipopolysaccharide (LPS) assembly . The YeaD protein has been crystallized . Sequence similarity suggests that YeaD may contain β-barrel structure(s) .

## Biological Role

Repressed by cra (protein.P0ACP1). Activated by rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39173|protein.P39173]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=yeaD; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=yeaD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005923,ECOCYC:G6966,GeneID:946572`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1863850-1864734:+; feature_type=gene
