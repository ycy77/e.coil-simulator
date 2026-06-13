---
entity_id: "gene.b4539"
entity_type: "gene"
name: "yoeB"
source_database: "NCBI RefSeq"
source_id: "gene-b4539"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4539"
  - "yoeB"
---

# yoeB

`gene.b4539`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4539`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yoeB (gene.b4539) is a gene entity. It encodes yoeB (protein.P69348). Encoded protein function: FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. Its mode of function is controversial; it has been proposed to be an mRNA interferase but also an inhibitor of translation initiation. When overproduced in wild-type cells, inhibits bacterial growth and translation by cleavage of mRNA molecules while it has a weak effect on colony forming ability. Overproduction of Lon protease specifically activates YoeB-dependent mRNA cleavage, leading to lethality. YefM binds to the promoter region of the yefM-yeoB operon to repress transcription, YeoB acts as a corepressor.; FUNCTION: Shown in vitro to be an mRNA interferase that requires translation for substrate cleavage; if the mRNA is mutated so as to not be translatable it is no longer cleaved. Cleavage only occurs within translated regions. Has RNase activity and preferentially cleaves at the 3'-end of purine ribonucleotides. {ECO:0000269|PubMed:16109374}.; FUNCTION: Also shown in vitro to be a translation initiation blocker. Binds to the 70S ribosome and 50S ribosomal subunit; binding is inhibited by hygromycin A and tetracycline, both of which bind to the 30S subunit in the A site...

## Biological Role

Repressed by yefM (protein.P69346), nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69348|protein.P69348]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yoeB; function=+
- `represses` <-- [[protein.P69346|protein.P69346]] `RegulonDB` `C` - regulator=YefM; target=yoeB; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yoeB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0285060,ECOCYC:G0-9121,GeneID:1450274`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2089211-2089465:-; feature_type=gene
