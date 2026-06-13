---
entity_id: "gene.b2804"
entity_type: "gene"
name: "fucU"
source_database: "NCBI RefSeq"
source_id: "gene-b2804"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2804"
  - "fucU"
---

# fucU

`gene.b2804`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2804`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fucU (gene.b2804) is a gene entity. It encodes fucU (protein.P0AEN8). Encoded protein function: FUNCTION: Involved in the anomeric conversion of L-fucose. Catalyzes also the interconversion of beta-pyran and beta-furan forms of D-ribose. {ECO:0000269|PubMed:15060078, ECO:0000269|PubMed:19524593}. EcoCyc product frame: EG10355-MONOMER. Genomic coordinates: 2938888-2939310. EcoCyc protein note: Utilizing NMR techniques, FucU was shown to catalyze the anomeric conversion of fucose. The enzyme also exhibits pyranase activity (catalyzing the interconversion of the pyranose and furanose forms) for D-ribose . FucU was previously shown to be an L-fucose binding protein with a KD for L-fucose of 1.61 mM . A crystal structure of FucU bound to L-fucose has been solved, showing a decameric toroidal structure that can be viewed as a pentamer of homodimers. Two adjacent subunits contribute to each active site. Site-directed mutagenesis of potential active site residues showed that Tyr111, His22, and Asp64 are required for catalytic activity. A reaction mechanism was proposed . Overexpression of FucU leads to increased resistance against xanthorrhizol .

## Biological Role

Activated by crp (protein.P0ACJ8), ygfI (protein.P52044).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEN8|protein.P0AEN8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=fucU; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=fucU; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009193,ECOCYC:EG10355,GeneID:945842`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2938888-2939310:+; feature_type=gene
