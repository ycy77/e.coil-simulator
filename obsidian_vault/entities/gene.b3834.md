---
entity_id: "gene.b3834"
entity_type: "gene"
name: "ubiJ"
source_database: "NCBI RefSeq"
source_id: "gene-b3834"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3834"
  - "ubiJ"
---

# ubiJ

`gene.b3834`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3834`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ubiJ (gene.b3834) is a gene entity. It encodes ubiJ (protein.P0ADP7). Encoded protein function: FUNCTION: Required for ubiquinone (coenzyme Q) biosynthesis under aerobic conditions (PubMed:24142253, PubMed:30686758). Binds hydrophobic ubiquinone biosynthetic intermediates via its SCP2 domain and is essential for the stability of the Ubi complex (PubMed:30686758). May constitute a docking platform where Ubi enzymes assemble and access their SCP2-bound polyprenyl substrates (PubMed:30686758). {ECO:0000269|PubMed:24142253, ECO:0000269|PubMed:30686758}. EcoCyc product frame: EG11474-MONOMER. EcoCyc synonyms: yigP. Genomic coordinates: 4019624-4020229. EcoCyc protein note: UbiJ is an accessory factor in ubiquinone biosynthesis that is part of the Ubi complex metabolon . The C terminus of UbiJ interacts directly with UbiK; the isolated proteins appear to form a 2:1 UbiK:UbiJ heterotrimer that is able to bind palmitoleate , ubiquinone-8, 2-octaprenylphenol, and C6-demethoxy-ubiquinone-8 . The N-terminal SCP2 domain of UbiJ is responsible for lipid binding . UbiJ predominantly localizes to the cytosol. The seven ubiquinone biosynthesis proteins UbiE, UbiF, UbiG, UbiH, UbiI, UbiJ, and UbiK form a 1 MDa complex in the cytosol; UbiJ appears to be required for stability of the complex . The purified SCP2 domain of UbiJ homodimerizes; crystal structures of this domain have been solved...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADP7|protein.P0ADP7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012536,ECOCYC:EG11474,GeneID:948915`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4019624-4020229:+; feature_type=gene
