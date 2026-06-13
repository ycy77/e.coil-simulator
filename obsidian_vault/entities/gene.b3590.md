---
entity_id: "gene.b3590"
entity_type: "gene"
name: "selB"
source_database: "NCBI RefSeq"
source_id: "gene-b3590"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3590"
  - "selB"
---

# selB

`gene.b3590`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3590`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

selB (gene.b3590) is a gene entity. It encodes selB (protein.P14081). Encoded protein function: FUNCTION: Translation factor necessary for the incorporation of selenocysteine into proteins. It probably replaces EF-Tu for the insertion of selenocysteine directed by the UGA codon. SelB binds GTP and GDP. EcoCyc product frame: EG10942-MONOMER. EcoCyc synonyms: fdhA. Genomic coordinates: 3758017-3759861. EcoCyc protein note: SelB is a specialized translation factor that takes the place of elongation factor EF-Tu for the insertion of selenocysteine into a peptide chain at the site of a UGA codon. Most UGA codons signal chain termination; a UGA codon that encodes selenocysteine insertion is distinguished from those that signal chain termination by a structured sequence, called SECIS (SElenoCysteine Insertion Sequence), immediately downstream of the UGA codon . SelB recognizes and binds to identical bases within the loop region in the SECIS hairpin structure of both fdhF and fdnG mRNAs, and thereby brings the charged modified-charged-selC-tRNA selenocysteyl-tRNASec (Sec-tRNASec) into the neighborhood of the UGA codon . Structures of several intermediates during delivery of Sec-tRNASec to the ribosome have been solved by single-particle cryo-electron microscopy, elucidating the dynamics of codon recognition and GTPase activation...

## Biological Role

Repressed by selB (protein.P14081).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P14081|protein.P14081]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P14081|protein.P14081]] `RegulonDB` `C` - regulator=SelB-L-selenocysteinyl-tRNA<sup>sec</sup>; target=selB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011729,ECOCYC:EG10942,GeneID:948103`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3758017-3759861:-; feature_type=gene
