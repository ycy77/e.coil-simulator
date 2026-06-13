---
entity_id: "protein.P0AFL3"
entity_type: "protein"
name: "ppiA"
source_database: "UniProt"
source_id: "P0AFL3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:2190212}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ppiA rot rotA b3363 JW3326"
---

# ppiA

`protein.P0AFL3`

## Static

- Type: `protein`
- Source: `UniProt:P0AFL3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:2190212}.

## Enriched Summary

FUNCTION: PPIases accelerate the folding of proteins (Probable). It catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides (PubMed:2190212). {ECO:0000269|PubMed:2190212, ECO:0000305}. PpiA is a peptidyl-prolyl cis-trans-isomerase (PPIase), catalyzing the conformational isomerization of prolyl residues in peptides. Cis-trans isomerization of prolyl peptide bonds is a slow step in protein folding, and thus PpiA is thought to facilitate proper protein folding. PpiA was shown to catalyze the refolding of denatured type III collagen . PpiA is a homolog of the human enzyme cyclophilin; unlike that enzyme, PpiA activity is only inhibited by high concentrations of cyclosporin A or FK506 . An F112W mutant, changing to the tryptophan residue conserved in eukaryotic cylcophilins, is more sensitive to inhibition by cyclosporin A and binds cylcosporin A in a configuration similar to the human enzyme . Solution structures of wild type and mutant PpiA as well as crystal structures of a mutant form of PpiA in a complex with a peptide containing the trans form of proline have been determined . A ppiA null mutant shows no apparent growth defect . A strain containing null mutations in all four known periplasmic peptidyl-prolyl cis-trans-isomerases, ppiA, ppiD, fkpA, and surA, is viable, but shows a decreased growth rate and increased antibiotic susceptibility...

## Biological Role

Catalyzes PEPTIDYLPROLYL-ISOMERASE-RXN (reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco03250` Viral life cycle - HIV-1 (KEGG)

## Annotation

FUNCTION: PPIases accelerate the folding of proteins (Probable). It catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides (PubMed:2190212). {ECO:0000269|PubMed:2190212, ECO:0000305}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco03250` Viral life cycle - HIV-1 (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN|reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3363|gene.b3363]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFL3`
- `KEGG:ecj:JW3326;eco:b3363;ecoc:C3026_18265;`
- `GeneID:93778634;947870;`
- `GO:GO:0003755; GO:0006457; GO:0030288; GO:0042597`
- `EC:5.2.1.8`

## Notes

Peptidyl-prolyl cis-trans isomerase A (PPIase A) (EC 5.2.1.8) (Cyclophilin A) (Rotamase A)
