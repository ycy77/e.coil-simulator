---
entity_id: "protein.P0AEM0"
entity_type: "protein"
name: "fkpB"
source_database: "UniProt"
source_id: "P0AEM0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fkpB slpA yaaD b0028 JW0026"
---

# fkpB

`protein.P0AEM0`

## Static

- Type: `protein`
- Source: `UniProt:P0AEM0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: PPIases accelerate the folding of proteins (Probable). Substrate specificity investigated with 'Suc-Ala-Xaa-Pro-Phe-4-nitroanilide' where Xaa is the amino acid tested, was found to be Phe > Leu >> Ile > Lys = Ala > Trp > His >> Gln (PubMed:9188461). {ECO:0000269|PubMed:9188461, ECO:0000305}. FkpB is a peptidyl-prolyl cis-trans isomerase (PPIase) of the FK506-binding protein type . FkpB also has chaperone activity; a number of ribosomal proteins appear to be natural substrates . Substrates were identified by pull-down assay and binding affinity measurements and include RpoE, RseA, RpsB and AphC . A crystal structure has been solved at 1.35 Å resolution. Serendipidously, the linker region of the purification tag of a different FkpB polypeptide is found in the chaperone binding groove of the insert-in-flap (IF) domain of FkpB, mimicing a chaperone substrate. A proline residue within the linker peptide appears to be specifically recognized and is important for binding . A solution structure of FkpB suggested that the orientation of the F37 residue is a reason for the moderate PPIase activity of FkpB; domain-swap experiments support this interpretation . Mutants in potential active site residues were assayed for potential substrate binding and PPIase activity...

## Biological Role

Catalyzes PEPTIDYLPROLYL-ISOMERASE-RXN (reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN).

## Annotation

FUNCTION: PPIases accelerate the folding of proteins (Probable). Substrate specificity investigated with 'Suc-Ala-Xaa-Pro-Phe-4-nitroanilide' where Xaa is the amino acid tested, was found to be Phe > Leu >> Ile > Lys = Ala > Trp > His >> Gln (PubMed:9188461). {ECO:0000269|PubMed:9188461, ECO:0000305}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN|reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0028|gene.b0028]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEM0`
- `KEGG:ecj:JW0026;eco:b0028;ecoc:C3026_00135;`
- `GeneID:86944962;93777408;944807;`
- `GO:GO:0003755; GO:0005829; GO:0042026`
- `EC:5.2.1.8`

## Notes

FKBP-type 16 kDa peptidyl-prolyl cis-trans isomerase (PPIase) (EC 5.2.1.8) (Rotamase)
