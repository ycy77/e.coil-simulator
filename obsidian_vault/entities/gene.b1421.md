---
entity_id: "gene.b1421"
entity_type: "gene"
name: "trg"
source_database: "NCBI RefSeq"
source_id: "gene-b1421"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1421"
  - "trg"
---

# trg

`gene.b1421`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1421`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trg (gene.b1421) is a gene entity. It encodes trg (protein.P05704). Encoded protein function: FUNCTION: Mediates taxis to the sugars ribose and galactose via an interaction with the periplasmic ribose- or galactose-binding proteins.; FUNCTION: Chemotactic-signal transducers respond to changes in the concentration of attractants and repellents in the environment, transduce a signal from the outside to the inside of the cell, and facilitate sensory adaptation through the variation of the level of methylation. Attractants increase the level of methylation while repellents decrease the level of methylation, the methyl groups are added by the methyltransferase CheR and removed by the methylesterase CheB. EcoCyc product frame: TRG-MONOMER. Genomic coordinates: 1492470-1494110.

## Biological Role

Activated by crp (protein.P0ACJ8), fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05704|protein.P05704]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=trg; function=+
- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=trg; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004744,ECOCYC:EG11018,GeneID:945995`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1492470-1494110:+; feature_type=gene
