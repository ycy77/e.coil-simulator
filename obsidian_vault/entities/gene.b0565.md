---
entity_id: "gene.b0565"
entity_type: "gene"
name: "ompT"
source_database: "NCBI RefSeq"
source_id: "gene-b0565"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0565"
  - "ompT"
---

# ompT

`gene.b0565`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0565`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ompT (gene.b0565) is a gene entity. It encodes ompT (protein.P09169). Encoded protein function: FUNCTION: Protease that can cleave T7 RNA polymerase, ferric enterobactin receptor protein (FEP), antimicrobial peptide protamine and other proteins. This protease has a specificity for paired basic residues. {ECO:0000269|PubMed:9683502}. EcoCyc product frame: EG10673-MONOMER. Genomic coordinates: 584680-585633. EcoCyc protein note: OmpT is an outer membrane protease with specificity for paired basic residues ; detailed studies on substrate specificity have been performed . OmpT is active under extreme denaturing conditions and shows a preference for denatured substrates . It is responsible for hydrolysis of the antimicrobial peptide protamine and is a virulence determinant in urinary tract infections . OmpT activity is cooperatively modulated by EG10669-MONOMER OmpA and lipopolysaccharide in vitro . OmpT cleaves endonuclease colicin E2 (ColE2), a bacteriocidal protein, and the associated cognate immunity protein (Im2) in the presence of BtuB; specifically, OmpT cleaves the C-terminal DNase domain of ColE2 . OmpT can cleave active human complement component C3 Kinetic parameters of the purified protein have been determined . Based on information from a crystal structure, a novel catalytic mechanism was suggested...

## Biological Role

Repressed by omrA (gene.b4444), omrB (gene.b4445), nac (protein.Q47005). Activated by lrp (protein.P0ACJ0), phoP (protein.P23836).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09169|protein.P09169]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `C` - regulator=PhoP; target=ompT; function=+
- `represses` <-- [[gene.b4444|gene.b4444]] `RegulonDB` `S` - regulator=OmrA; target=ompT; function=-
- `represses` <-- [[gene.b4445|gene.b4445]] `RegulonDB` `S` - regulator=OmrB; target=ompT; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ompT; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001931,ECOCYC:EG10673,GeneID:945185`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:584680-585633:-; feature_type=gene
