---
entity_id: "gene.b1116"
entity_type: "gene"
name: "lolC"
source_database: "NCBI RefSeq"
source_id: "gene-b1116"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1116"
  - "lolC"
---

# lolC

`gene.b1116`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1116`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lolC (gene.b1116) is a gene entity. It encodes lolC (protein.P0ADC3). Encoded protein function: FUNCTION: Part of an ATP-dependent transport system LolCDE responsible for the release of lipoproteins targeted to the outer membrane from the inner membrane. Such a release is dependent of the sorting-signal (absence of an Asp at position 2 of the mature lipoprotein) and of LolA. EcoCyc product frame: YCFU-MONOMER. EcoCyc synonyms: ycfU. Genomic coordinates: 1175427-1176626. EcoCyc protein note: LolC is an inner membrane subunit of the LolCDE lipoprotein release complex . LolC contains 4 predicted transmembrane regions; a large loop region between the first and second transmembrane regions is located in the periplasm . The periplasmic domain of LolC contains structural features that underpin the mechanotransmission mechanism of the type VII ABC transporter, MACB "MacB" . The periplasmic domain of LolC contains a 'hook' (residues P167 - P179) and 'pad' (R163, Q181, R182) that mediate interaction with the lipopotein chaperone G6465-MONOMER LolA; the interaction between LolA and LolCDE occurs exclusively through LolC and is independent of nucleotide binding and hydrolysis; LolC discriminates between LolA and LolB (see also ).

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADC3|protein.P0ADC3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=lolC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003772,ECOCYC:G6573,GeneID:945673`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1175427-1176626:+; feature_type=gene
