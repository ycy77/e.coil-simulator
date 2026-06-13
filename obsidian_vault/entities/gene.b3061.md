---
entity_id: "gene.b3061"
entity_type: "gene"
name: "ttdA"
source_database: "NCBI RefSeq"
source_id: "gene-b3061"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3061"
  - "ttdA"
---

# ttdA

`gene.b3061`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3061`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ttdA (gene.b3061) is a gene entity. It encodes ttdA (protein.P05847). Encoded protein function: L(+)-tartrate dehydratase subunit alpha (L-TTD alpha) (EC 4.2.1.32) EcoCyc product frame: TTDA-MONOMER. EcoCyc synonyms: ygjA. Genomic coordinates: 3206463-3207374. EcoCyc protein note: The ttdA gene encodes the α subunit of L-tartrate dehydratase . Transcription of ttdA is activated by the LysR-type transcriptional activator TtdR in the presence of L-tartrate or meso-tartrate and is repressed by O2 and nitrate. Binding of TtdR to the ttdA-ttdR intergenic region has been shown . Anaerobic induction depends on FNR . TtdA appears to be involved in biofilm formation. A ΔttdA mutant shows a significant decrease in biofilm formation. Deletion of tqsA increases biofilm formation and increases expression of ttdA 11-fold . TtdA: "L-tartrate dehydratase A"

## Biological Role

Repressed by glaR (protein.P37338). Activated by ttdR (protein.P45463).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05847|protein.P05847]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P45463|protein.P45463]] `RegulonDB` `S` - regulator=Dan; target=ttdA; function=+
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ttdA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010050,ECOCYC:EG11168,GeneID:947565`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3206463-3207374:+; feature_type=gene
