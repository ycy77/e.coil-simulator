---
entity_id: "protein.P31979"
entity_type: "protein"
name: "nuoF"
source_database: "UniProt"
source_id: "P31979"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nuoF b2284 JW2279"
---

# nuoF

`protein.P31979`

## Static

- Type: `protein`
- Source: `UniProt:P31979`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. NuoF is part of the soluble fragment of NADH dehydrogenase I, which represents the electron input part of the enzyme . Based on sequence similarity, NuoF contains the FMN and NADH binding sites . Site-directed mutagenesis of the E95 residue in the predicted NADH binding site led to altered binding of NADH and inhibition by NAD+, and a change in the midpoint potential of the FMN cofactor in Complex I . The E95Q mutation may distort the catalytic site and thereby retard the hydride transfer from NADH to FMN . NADH-dependent production of hydrogen peroxide is increased in the E95Q mutant . NuoF was shown to contain the N3 4Fe-4S cluster; the cysteine residues responsible for ligation of the 4Fe-4S cluster were identified by site-directed mutagenesis . Evolved E. coli strains that are adapted to higher production of NADPH contain an E183A mutation in NuoF; NDH-1 containing this subunit is able to oxidize both NADH and NADPH...

## Biological Role

Catalyzes NADH:ubiquinone oxidoreductase (reaction.R11945). Component of NADH:quinone oxidoreductase I, peripheral arm (complex.ecocyc.CPLX0-3361), NADH:quinone oxidoreductase I (complex.ecocyc.NADH-DHI-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R11945|reaction.R11945]] `KEGG` `database` - via EC:7.1.1.2
- `is_component_of` --> [[complex.ecocyc.CPLX0-3361|complex.ecocyc.CPLX0-3361]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.NADH-DHI-CPLX|complex.ecocyc.NADH-DHI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2284|gene.b2284]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31979`
- `KEGG:ecj:JW2279;eco:b2284;ecoc:C3026_12745;`
- `GeneID:946753;`
- `GO:GO:0005886; GO:0008137; GO:0009060; GO:0010181; GO:0016020; GO:0022904; GO:0030964; GO:0045271; GO:0045333; GO:0046872; GO:0048038; GO:0051287; GO:0051539`
- `EC:7.1.1.-`

## Notes

NADH-quinone oxidoreductase subunit F (EC 7.1.1.-) (NADH dehydrogenase I subunit F) (NDH-1 subunit F) (NUO6)
