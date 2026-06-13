---
entity_id: "gene.b4311"
entity_type: "gene"
name: "nanC"
source_database: "NCBI RefSeq"
source_id: "gene-b4311"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4311"
  - "nanC"
---

# nanC

`gene.b4311`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4311`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nanC (gene.b4311) is a gene entity. It encodes nanC (protein.P69856). Encoded protein function: FUNCTION: Outer membrane channel protein allowing the entry of N-acetylneuraminic acid (Neu5Ac, the most abundant sialic acid on host cell surfaces) into the bacteria (PubMed:15743943, PubMed:22246445). NanC proteins form high-conductance channels which are open at low membrane potentials and which have a weak anion selectivity (PubMed:15743943). {ECO:0000269|PubMed:15743943, ECO:0000269|PubMed:22246445}. EcoCyc product frame: G7921-MONOMER. EcoCyc synonyms: yjhA. Genomic coordinates: 4538785-4539501. EcoCyc protein note: nanC encodes an N-acetylneuraminic acid-inducible outer membrane channel; purified NanC reconstituted into liposomes functions as a voltage-dependent, high-conductance channel with weak anion selectivity (see further ); NanC is necessary for growth on N-acetylneuraminic acid (NeuNAc) as a carbon source when the general porins OmpF and OmpC are absent . In the crystal structure reported by NanC forms a barrel composed of 12-antiparallel β-strands with a transmembrane channel whose properties are well suited for the translocation of acidic oligosaccharides. nanC forms a putative operon with nanM and nanS. Expression of nanC is induced by NeuNAc and is modulated by N-acetylglucosamine...

## Biological Role

Repressed by spf (gene.b3864), nanR (protein.P0A8W0), nagC (protein.P0AF20). Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69856|protein.P69856]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=nanC; function=+
- `represses` <-- [[gene.b3864|gene.b3864]] `RegulonDB` `S` - regulator=Spf; target=nanC; function=-
- `represses` <-- [[protein.P0A8W0|protein.P0A8W0]] `RegulonDB` `C` - regulator=NanR; target=nanC; function=-
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `C` - regulator=NagC; target=nanC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014136,ECOCYC:G7921,GeneID:946843`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4538785-4539501:-; feature_type=gene
