---
entity_id: "gene.b3857"
entity_type: "gene"
name: "mobA"
source_database: "NCBI RefSeq"
source_id: "gene-b3857"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3857"
  - "mobA"
---

# mobA

`gene.b3857`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3857`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mobA (gene.b3857) is a gene entity. It encodes mobA (protein.P32173). Encoded protein function: FUNCTION: Transfers a GMP moiety from GTP to Mo-molybdopterin (Mo-MPT) cofactor (Moco or molybdenum cofactor) to form Mo-molybdopterin guanine dinucleotide (Mo-MGD) cofactor. Is also involved in the biosynthesis of the bis-MGD form of the Moco cofactor (Mo-bisMGD) in which the metal is symmetrically ligated by the dithiolene groups of two MGD molecules. Is necessary and sufficient for the in vitro activation of the DMSOR molybdoenzyme that uses the Mo-bisMGD form of molybdenum cofactor, which implies formation and efficient insertion of the cofactor into the enzyme without the need of a chaperone. Is specific for GTP since other nucleotides such as ATP and GMP cannot be utilized. {ECO:0000269|PubMed:10978348, ECO:0000269|PubMed:1648082, ECO:0000269|PubMed:21081498, ECO:0000269|PubMed:8020507}. EcoCyc product frame: EG11829-MONOMER. EcoCyc synonyms: chlB, mob, narB. Genomic coordinates: 4041415-4041999. EcoCyc protein note: MobA is required for the biosynthesis of the molybdopterin guanine dinucleotide (MGD) cofactor . The enzyme catalyzes the transfer of a GMP moiety from GTP to Mo-molybdopterin, forming MGD . The MGD cofactor can be further modified to CPD-15873 "bis-MGD"...

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32173|protein.P32173]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=mobA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012593,ECOCYC:EG11829,GeneID:948349`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4041415-4041999:-; feature_type=gene
