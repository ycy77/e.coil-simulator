---
entity_id: "gene.b0675"
entity_type: "gene"
name: "umpH"
source_database: "NCBI RefSeq"
source_id: "gene-b0675"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0675"
  - "umpH"
---

# umpH

`gene.b0675`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0675`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

umpH (gene.b0675) is a gene entity. It encodes nagD (protein.P0AF24). Encoded protein function: FUNCTION: Catalyzes the dephosphorylation of an unusually broad range of substrate including deoxyribo- and ribonucleoside tri-, di-, and monophosphates, as well as polyphosphate and glucose-1-P (Glu1P). {ECO:0000269|PubMed:16430214, ECO:0000269|PubMed:16990279}. EcoCyc product frame: EG10634-MONOMER. EcoCyc synonyms: nagD. Genomic coordinates: 699574-700326. EcoCyc protein note: UmpH is a ribonucleoside tri-, di-, and monophosphatase with a preference for purines . The enzyme was found to degrade "overflow" UMP nucleotides and is required for optimal growth in response to environmental pyrimidine intermediates . UMP accumulation to levels above the Km of the enzyme, triggered by environmental conditions or artificially induced by mutations in the normal feedback regulation of the pyrimidine biosynthesis pathway, appear to cause the overflow degradation of UMP by UmpH . Though UmpH is a member of the nag N-acetylglucosamine utilization operon, it is a fairly general ribonucleotide monophosphatase . A type IIA member of the HAD protein superfamily, UmpH shows peak activity with UMP, but is also a very effective phosphatase with AMP, GMP and CMP . The structure of UmpH has been solved to 1.8 Å resolution...

## Biological Role

Repressed by crp (protein.P0ACJ8), nagC (protein.P0AF20). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF24|protein.P0AF24]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=umpH; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=umpH; function=-+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=umpH; function=-+
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `C` - regulator=NagC; target=umpH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002296,ECOCYC:EG10634,GeneID:945283`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:699574-700326:-; feature_type=gene
