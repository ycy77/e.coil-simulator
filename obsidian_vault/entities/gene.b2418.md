---
entity_id: "gene.b2418"
entity_type: "gene"
name: "pdxK"
source_database: "NCBI RefSeq"
source_id: "gene-b2418"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2418"
  - "pdxK"
---

# pdxK

`gene.b2418`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2418`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pdxK (gene.b2418) is a gene entity. It encodes pdxK (protein.P40191). Encoded protein function: FUNCTION: B6-vitamer kinase involved in the salvage pathway of pyridoxal 5'-phosphate (PLP). Catalyzes the phosphorylation of pyridoxine (PN), pyridoxal (PL), and pyridoxamine (PM), forming their respective 5'-phosphorylated esters, i.e. PNP, PLP and PMP. {ECO:0000269|PubMed:15249053, ECO:0000269|PubMed:9537380}. EcoCyc product frame: PDXK-MONOMER. EcoCyc synonyms: yfeI, pdxL. Genomic coordinates: 2536386-2537237. EcoCyc protein note: Pyridoxal kinase 1 is able to phosphorylate pyridoxal (PL), pyridoxine (PN), pyridoxamine (PM), and hydroxymethylpyrimidine (HMP), forming their respective 5'-phosphoesters . There are two pyridoxal kinases in E. coli: the enzyme described here (PdxK), and a second enzyme, PDXY-MONOMER PdxY . PdxK is the major PL kinase activity in the cell . Both enzymes function in the scavenger/salvage pathway of pyridoxal 5'-phosphate (PLP) . The HMP kinase activity of PdxK contributes to thiamine salvage . Under physiological conditions, MgATP is the favored cosubstrate over ZnATP . Potassium is required for catalytic activity; kinetic and inhibitor studies suggest a sequential random addition of the substrates...

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P40191|protein.P40191]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=pdxK; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007973,ECOCYC:G7259,GeneID:946881`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2536386-2537237:-; feature_type=gene
