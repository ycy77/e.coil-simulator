---
entity_id: "gene.b1415"
entity_type: "gene"
name: "aldA"
source_database: "NCBI RefSeq"
source_id: "gene-b1415"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1415"
  - "aldA"
---

# aldA

`gene.b1415`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1415`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aldA (gene.b1415) is a gene entity. It encodes aldA (protein.P25553). Encoded protein function: FUNCTION: Catalyzes the irreversible oxidation of L-lactaldehyde to L-lactate (PubMed:27671251, PubMed:3298215, PubMed:3308886, PubMed:6345530). Also shows high activity with glycolaldehyde and L-glyceraldehyde (PubMed:16731973, PubMed:31850327, PubMed:3275622, PubMed:3308886, PubMed:6345530). Has weaker activity with various aldehydes such as methylglyoxal, propionaldehyde or benzaldehyde (PubMed:16731973, PubMed:3308886). Involved in the degradation of lactaldehyde produced during metabolism of L-fucose and L-rhamnose (PubMed:3275622, PubMed:3298215). It may be involved in several other metabolic pathways (PubMed:3308886). {ECO:0000269|PubMed:16731973, ECO:0000269|PubMed:27671251, ECO:0000269|PubMed:31850327, ECO:0000269|PubMed:3275622, ECO:0000269|PubMed:3298215, ECO:0000269|PubMed:3308886, ECO:0000269|PubMed:6345530}. EcoCyc product frame: LACTALDDEHYDROG-MONOMER. EcoCyc synonyms: ald. Genomic coordinates: 1488232-1489671. EcoCyc protein note: Aldehyde dehydrogenase A (AldA) is an NAD+-dependent dehydrogenase of relatively broad specificity for small α-hydroxyaldehyde substrates. It is thus utilized in several metabolic pathways...

## Biological Role

Repressed by dnaA (protein.P03004), arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25553|protein.P25553]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=aldA; function=+
- `represses` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `S` - regulator=DnaA; target=aldA; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `C` - regulator=ArcA; target=aldA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004725,ECOCYC:EG10035,GeneID:945672`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1488232-1489671:+; feature_type=gene
