---
entity_id: "gene.b1300"
entity_type: "gene"
name: "puuC"
source_database: "NCBI RefSeq"
source_id: "gene-b1300"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1300"
  - "puuC"
---

# puuC

`gene.b1300`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1300`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

puuC (gene.b1300) is a gene entity. It encodes puuC (protein.P23883). Encoded protein function: FUNCTION: Catalyzes the oxidation of 3-hydroxypropionaldehyde (3-HPA) to 3-hydroxypropionic acid (3-HP) (PubMed:18668238). It acts preferentially with NAD but can also use NADP (PubMed:18668238). 3-HPA appears to be the most suitable substrate for PuuC followed by isovaleraldehyde, propionaldehyde, butyraldehyde, and valeraldehyde (PubMed:18668238). It might play a role in propionate and/or acetic acid metabolisms (PubMed:18668238). Also involved in the breakdown of putrescine through the oxidation of gamma-Glu-gamma-aminobutyraldehyde to gamma-Glu-gamma-aminobutyrate (gamma-Glu-GABA) (PubMed:15590624). {ECO:0000269|PubMed:15590624, ECO:0000269|PubMed:18668238, ECO:0000305|PubMed:1840553}. EcoCyc product frame: ALDHDEHYDROG-MONOMER. EcoCyc synonyms: aldH. Genomic coordinates: 1362743-1364230. EcoCyc protein note: The puuC gene was first reported as a gene encoding a putative aldehyde dehydrogenase of unknown function. The product of the gene shares 40% identity and over 60% similarity, with both the cytosolic and the mitochondrial forms of mammalian aldehyde dehydrogenases . It was later inferred to be the γ-glutamyl-γ-aminobutyraldehyde dehydrogenase in a putrescine utilization pathway; together with PuuB, γ-glutamyl-γ-aminobutyrate is produced from γ-glutamylputrescine...

## Biological Role

Repressed by puuR (protein.P0A9U6). Activated by fimZ (protein.P0AEL8).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23883|protein.P23883]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AEL8|protein.P0AEL8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9U6|protein.P0A9U6]] `RegulonDB` `S` - regulator=PuuR; target=puuC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004376,ECOCYC:EG10036,GeneID:947003`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1362743-1364230:+; feature_type=gene
