---
entity_id: "gene.b2721"
entity_type: "gene"
name: "hycE"
source_database: "NCBI RefSeq"
source_id: "gene-b2721"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2721"
  - "hycE"
---

# hycE

`gene.b2721`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2721`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hycE (gene.b2721) is a gene entity. It encodes hycE (protein.P16431). Encoded protein function: Formate hydrogenlyase subunit 5 (FHL subunit 5) (Hydrogenase-3 component E) EcoCyc product frame: HYCELARGE-MONOMER. EcoCyc synonyms: hevE. Genomic coordinates: 2844762-2846471. EcoCyc protein note: The hycBCDEFG genes in E. coli K-12 encode the hydrogenase component (hydrogenase 3) of the formate hydrogenlyase complex. HycE is the large subunit of hydrogenase 3 ; it contains the nickel-iron active site where protons are reduced to H2 (see ). Maturation of HycE requires incorporation of nickel followed by processing after the Arg537 residue by the HycI maturation endopeptidase . Maturation has been reconstituted in vitro and requires HypB, HypC, HypD, HypE, HypF, HycI and nickel, as it does in vivo . HypC interacts directly with pre-HycE and facilitates metal incorporation ; mutational studies of conserved cysteine residues have led to a model for nickel incorporation . After the incorporation of nickel, pre-HycE must dissociate from HypC to become a substrate for the HycI maturation endopeptidase . HycE variants with increased hydrogen-producing activity have been engineered .

## Biological Role

Activated by modE (protein.P0A9G8), fhlA (protein.P19323), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16431|protein.P16431]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=hycE; function=+
- `activates` <-- [[protein.P19323|protein.P19323]] `RegulonDB` `S` - regulator=FhlA; target=hycE; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=hycE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008944,ECOCYC:EG10478,GeneID:947396`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2844762-2846471:-; feature_type=gene
