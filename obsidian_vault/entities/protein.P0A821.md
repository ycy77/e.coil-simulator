---
entity_id: "protein.P0A821"
entity_type: "protein"
name: "selA"
source_database: "UniProt"
source_id: "P0A821"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "selA fdhA b3591 JW3564"
---

# selA

`protein.P0A821`

## Static

- Type: `protein`
- Source: `UniProt:P0A821`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Converts seryl-tRNA(Sec) to selenocysteinyl-tRNA(Sec) required for selenoprotein biosynthesis. Requires selenophosphate as the selenium-donor molecule. {ECO:0000269|PubMed:2007584, ECO:0000269|PubMed:2007585}. Selenocysteine synthase (SelA) catalyzes the conversion of serine to selenocysteine on serine-charged tRNASec . SelA is a complex of 10 subunits with five-fold symmetry ; the homodecameric structure is assembled via stepwise addition of dimers to intermediate oligomeric states . Formation of a productive active site requires homodecamerization . The pyridoxal 5'-phosphate cofactor is present at a stoichiometry of one per monomer and is attached at Lys295 . The seryl-tRNASecUCA substrate was thought to be present at a stoichiometry of one per two monomers , but was later shown to be at a one-to-one stoichiometry . The serine residue of seryl-tRNASec first forms a Schiff base with the PLP cofactor, followed by dehydration of serine to generate the enzyme-bound aminoacrylyl-tRNASec intermediate . CPLX0-7957 SelD forms a ternary complex with the SelA-tRNASec complex . Structural analysis of a single-particle cryoEM reconstruction of SelA covalently bound to PLP at a resolution of 2.69 Å confirms the symmetrical, ring-like pentamer of dimers structure and estimates that 10 tRNASec molecules can potentially bind...

## Biological Role

Catalyzes selenophosphate:L-seryl-tRNASec selenium transferase (reaction.R08219). Component of selenocysteine synthase (complex.ecocyc.CPLX0-1141).

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Converts seryl-tRNA(Sec) to selenocysteinyl-tRNA(Sec) required for selenoprotein biosynthesis. Requires selenophosphate as the selenium-donor molecule. {ECO:0000269|PubMed:2007584, ECO:0000269|PubMed:2007585}.

## Pathways

- `eco00450` Selenocompound metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R08219|reaction.R08219]] `KEGG` `database` - via EC:2.9.1.1
- `is_component_of` --> [[complex.ecocyc.CPLX0-1141|complex.ecocyc.CPLX0-1141]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## Incoming Edges (1)

- `encodes` <-- [[gene.b3591|gene.b3591]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A821`
- `KEGG:ecj:JW3564;eco:b3591;`
- `GeneID:75204641;948124;`
- `GO:GO:0001514; GO:0001717; GO:0004125; GO:0005829; GO:0016260; GO:0030170; GO:0042802`
- `EC:2.9.1.1`

## Notes

L-seryl-tRNA(Sec) selenium transferase (EC 2.9.1.1) (Selenocysteine synthase) (Sec synthase) (Selenocysteinyl-tRNA(Sec) synthase)
