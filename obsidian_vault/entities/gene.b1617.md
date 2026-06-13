---
entity_id: "gene.b1617"
entity_type: "gene"
name: "uidA"
source_database: "NCBI RefSeq"
source_id: "gene-b1617"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1617"
  - "uidA"
---

# uidA

`gene.b1617`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1617`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uidA (gene.b1617) is a gene entity. It encodes uidA (protein.P05804). Encoded protein function: FUNCTION: Displays beta-glucuronidase activity with the artificial substrate p-nitrophenyl-beta-D-glucuronide (PNPG) and with 4-methylumbelliferyl-glucuronide (PubMed:21051639, PubMed:23690068, PubMed:26364932, PubMed:3105604, PubMed:33664385). Is likely capable of scavenging glucuronate from a range of chemically distinct xenobiotic and endobiotic glucuronides present in the gastrointestinal (GI) tract, to be able to utilize these diverse sources of carbon. As part of the GI microbiome, this enzyme is able to reactivate glucuronide drug conjugates, such reactivated compounds can significantly damage the GI tract (PubMed:26364932). {ECO:0000269|PubMed:21051639, ECO:0000269|PubMed:23690068, ECO:0000269|PubMed:26364932, ECO:0000269|PubMed:3105604, ECO:0000269|PubMed:33664385}. EcoCyc product frame: BETA-GLUCURONID-MONOMER. EcoCyc synonyms: gurA, gusA. Genomic coordinates: 1694260-1696071. EcoCyc protein note: β-D-glucuronidase catalyzes the cleavage of a wide variety of β-glucuronides . The enzyme is a homotetramer , but higher-order multimers have also been shown to be active . A number of crystal structures of the enzyme alone and bound to specific inhibitors have been solved . Reaction kinetics of single molecules have been measured and compared to values measured in bulk assays...

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05804|protein.P05804]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005410,ECOCYC:EG11055,GeneID:946149`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1694260-1696071:-; feature_type=gene
