---
entity_id: "gene.b4139"
entity_type: "gene"
name: "aspA"
source_database: "NCBI RefSeq"
source_id: "gene-b4139"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4139"
  - "aspA"
---

# aspA

`gene.b4139`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4139`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aspA (gene.b4139) is a gene entity. It encodes aspA (protein.P0AC38). Encoded protein function: FUNCTION: Catalyzes the reversible conversion of L-aspartate to fumarate and ammonia (PubMed:1897995, PubMed:2853974, PubMed:33012071, PubMed:4584395, PubMed:8047016, PubMed:8119980). In the reverse reaction, consumption of fumarate is observed in the presence of not only NH4(+), but also hydroxylamine (NH(2)OH) (PubMed:1897995, PubMed:4584395). Is specific for L-aspartate and cannot use structural analogs of L-aspartate such as D-aspartate, DL-alpha-methylaspartate, DL-beta-methylaspartate, DL-threo-beta-hydroxy-aspartate, DL-erythro-beta-hydroxyaspartate, L-cysteate, L-alpha-aminobutyrate, L-asparagine, L-alanine or L-glutamate (PubMed:4584395). Represents the central enzyme for nitrogen assimilation from L-aspartate in E.coli (PubMed:33012071). {ECO:0000269|PubMed:1897995, ECO:0000269|PubMed:2853974, ECO:0000269|PubMed:33012071, ECO:0000269|PubMed:4584395, ECO:0000269|PubMed:8047016, ECO:0000269|PubMed:8119980}. EcoCyc product frame: ASPARTASE-MONOMER. Genomic coordinates: 4366891-4368327.

## Biological Role

Repressed by lrp (protein.P0ACJ0), narL (protein.P0AF28). Activated by fnr (protein.P0A9E5), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC38|protein.P0AC38]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=aspA; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=aspA; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=aspA; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=aspA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013551,ECOCYC:EG10095,GeneID:948658`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4366891-4368327:-; feature_type=gene
