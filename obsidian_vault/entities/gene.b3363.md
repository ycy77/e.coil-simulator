---
entity_id: "gene.b3363"
entity_type: "gene"
name: "ppiA"
source_database: "NCBI RefSeq"
source_id: "gene-b3363"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3363"
  - "ppiA"
---

# ppiA

`gene.b3363`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3363`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ppiA (gene.b3363) is a gene entity. It encodes ppiA (protein.P0AFL3). Encoded protein function: FUNCTION: PPIases accelerate the folding of proteins (Probable). It catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides (PubMed:2190212). {ECO:0000269|PubMed:2190212, ECO:0000305}. EcoCyc product frame: EG10757-MONOMER. EcoCyc synonyms: rot, rotA. Genomic coordinates: 3491725-3492297. EcoCyc protein note: PpiA is a peptidyl-prolyl cis-trans-isomerase (PPIase), catalyzing the conformational isomerization of prolyl residues in peptides. Cis-trans isomerization of prolyl peptide bonds is a slow step in protein folding, and thus PpiA is thought to facilitate proper protein folding. PpiA was shown to catalyze the refolding of denatured type III collagen . PpiA is a homolog of the human enzyme cyclophilin; unlike that enzyme, PpiA activity is only inhibited by high concentrations of cyclosporin A or FK506 . An F112W mutant, changing to the tryptophan residue conserved in eukaryotic cylcophilins, is more sensitive to inhibition by cyclosporin A and binds cylcosporin A in a configuration similar to the human enzyme . Solution structures of wild type and mutant PpiA as well as crystal structures of a mutant form of PpiA in a complex with a peptide containing the trans form of proline have been determined . A ppiA null mutant shows no apparent growth defect...

## Biological Role

Repressed by crp (protein.P0ACJ8), cytR (protein.P0ACN7). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), cpxR (protein.P0AE88).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco03250` Viral life cycle - HIV-1 (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFL3|protein.P0AFL3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ppiA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ppiA; function=-+
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `C` - regulator=CpxR; target=ppiA; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ppiA; function=-+
- `represses` <-- [[protein.P0ACN7|protein.P0ACN7]] `RegulonDB` `S` - regulator=CytR; target=ppiA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010992,ECOCYC:EG10757,GeneID:947870`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3491725-3492297:-; feature_type=gene
